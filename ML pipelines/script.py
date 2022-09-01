import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA

from sklearn.metrics import confusion_matrix

from scipy.io import arff

data = arff.loadarff('bone-marrow.arff')
df = pd.DataFrame(data[0])
print(df.head(1))
#37 columns
print('columns:')
print(list(df.columns.values))

df.drop(columns=['Disease'], inplace=True)

#Convert all columns to numeric, coerce errors to null values
for c in df.columns:
    df[c] = pd.to_numeric(df[c], errors='coerce')
    
#Make sure binary columns are encoded as 0 and 1
for c in df.columns[df.nunique()==2]:
    df[c] = (df[c]==1)*1.0

#Calculate the number of unique values for each column
print('number of unique values in each columns:')
print(df.nunique())

#Set target - survival_status - as y; features (dropping survival status and time) as X
y = df['survival_status']
x = df.drop(columns = ['survival_time', 'survival_status'])

#Define lists of numeric and categorical columns based on number of unique values (>7 is numeric)
num_cols = x.columns[x.nunique()>7]
cat_cols = x.columns[x.nunique()<=7]

#Print columns with missing values
missing_val_col = x.columns[x.isnull().sum()>0]
print(missing_val_col)

#Split data into train/test split
x_train, x_test, y_train, y_test = train_test_split(x,y, random_state=0, test_size=0.2)

#Create categorical preprocessing pipeline & use mode to fill in missing values and OHE
cat_vals = Pipeline([("imputer",SimpleImputer(strategy='most_frequent')), ("ohe",OneHotEncoder(sparse=False, drop='first', handle_unknown = 'ignore'))])

#Create numerical preprocessing pipeline &use mean to fill in missing values and standard scaling of features
num_vals = Pipeline([("imputer",SimpleImputer(strategy='mean')), ("scale",StandardScaler())])

#Create column transformer to preprocess the numerical and categorical features separately
preprocess = ColumnTransformer( transformers=[ ("cat_process", cat_vals, cat_cols), ("num_process", num_vals, num_cols) ] )

#Create a pipeline with preprocess, PCA, and a logistic regresssion model
pipeline = Pipeline([("preprocess",preprocess), ("pca", PCA()), ("clf",LogisticRegression())])

#Fit the pipeline on the training data
pipeline.fit(x_train, y_train)
#Predict the pipeline on the test data
pipeline.score(x_test,y_test)

#Define search space of hyperparameters
search_space = [{'clf':[LogisticRegression()], 'clf__C': np.logspace(-4, 2, 10), 'pca__n_components':np.linspace(5,35,7).astype(int)},
                {'clf': [RandomForestClassifier()], 'clf__max_depth': np.linspace(2,20,10).astype(int), 'pca__n_components':np.linspace(5,35,7).astype(int)}]
#Search over hyperparameters abolve to optimize pipeline and fit
gs = GridSearchCV(pipeline, search_space, cv=5)
gs.fit(x_train, y_train)

#Save the best estimator from the gridsearch and print attributes and final accuracy on test set
best_model = gs.best_estimator_

#Print attributes of best_model
print('best classification model:')
print(best_model.named_steps['clf'])
print('hyperparameters of est classification model:')
print(best_model.named_steps['clf'].get_params())
print('number of components selected in the PCA step:')
print(best_model.named_steps['pca'].n_components)

#Print final accuracy score 
print('best model accuracy score:')
print(best_model.score(x_test,y_test))