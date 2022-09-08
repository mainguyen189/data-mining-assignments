Logistic regression and random forest


Logistic regression: predict the probability (0-1) of a datapoint belonging to a specific category, or classification
- binary classification.
- estimate the log odds that a datapoint belongs to the positive class -> probability.
- the coefficients of a logistic regression model can be used to estimate relative feature importance.
- A classification threshold is used to determine the probabilistic cutoff for where a data sample is classified as belonging to a positive or negative class. The default cutoff in sklearn is 0.5.


Random forest: ensemble machine learning model. 
- Makes classification by aggregating the classifications of many decision trees -> are used to avoid overfitting of decision tree
- Every decision tree in a random forest is created by using a different subset of data points from the training set. Those data points are chosen at random with replacement, which means a single data point can be chosen more than once. This process is known as bagging.
- When creating a tree in a random forest, a randomly selected subset of features are considered as candidates for the best splitting feature. If your dataset has n features, it is common practice to randomly select the square root of n features.

Evaluation: confusion matrix or classification report:
- Accuracy = (TP + TN)/(TP + FP + TN + FN)
= Precision = TP/(TP + FP)
- Recall = TP/(TP + FN)
- F1 score: weighted average of precision and recall
