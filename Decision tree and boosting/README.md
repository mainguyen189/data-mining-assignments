Boosted ensemble methods use weak learners as base models that are simple and tend to suffer from high bias. The weak learners underfit the data.

Boosting is a sequential learning technique where each of the base models builds off of the previous model. Each subsequent model aims to improve the performance of the final ensemble model by attempting to fix the errors in the previous stage.

Applying here to decision tree as base estimator because:
- easy to interpret decision tree
- training data requires very little manipulation (no need standardization, removal of collinearity, etc.)
Decision tree weaknesses:
- suffer from high variance and are therefore prone to overfitting
- makeseries of decisions which cause them to memorize the training data, so they do not generalize well to unseen data. 
