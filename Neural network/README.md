
- Preparing the data for learning
- separating features from labels using array slicing
- determining the shape of your data
- preprocessing the categorical variables using one-hot encoding
- splitting the data into training and test sets
- scaling the numerical features
- hyperparameter tuning
  + learning rate
  + batch size
  + number of epochs
  + model size (number of hidden layers/neurons and number of parameters)
  + regularization (dropout)



ROC curve gives us the relationship between our true positive rate and our false positive rate. A true positive would be correctly identifying a patient with Pneumonia, while a false positive would be incorrectly identifying a healthy person as having pneumonia. Like with accuracy, we want our AUC to be as close to 1.0 as possible.
