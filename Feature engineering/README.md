Feature selection methods:


Wrapper methods involve fitting a model and evaluating its performance for a particular subset of features. They work by using a search algorithm to find which combination of features can optimize the performance of a given model.

Advantages
- They can determine the optimal set of features that produce the best results for a specific machine learning problem.
- They can better account for multivariate relationships because model performance is evaluated.

Disadvantages
- They are computationally expensive because the model needs to be re-fitted for each feature set being tested.


Embedded methods also involve building and evaluating models for different feature subsets, but their feature selection process happens at the same time as their model fitting step.

Advantages
- Like wrapper methods, they can optimize the feature set for a particular model and account for multivariate relationships.
- They are also generally less computationally expensive because feature selection happens during model training.


Filter methods are the simplest type of feature selection method. They work by filtering features prior to model building based on some criteria.

Advantages
- They are computationally inexpensive, since they do not involve testing the subsetted features using a model.
- They can work for any type of machine learning model.

Disadvantages
- It is more difficult to take multivariate relationships into account because we are not evaluating model performance. For example, a variable might not have much predictive power on its own, but can be informative when combined with other variables.
- They are not tailored toward specific types of models.



# Hyperparameter tuning methods
- The grid search algorithm for hyperparameter tuning works by training a model on predetermined lists of hyperparameter values. Try every hyperparameter value on the list, and then use the one that makes the model perform best.
- The random search algorithm works similarly, but instead of using a predetermined list of hyperparameter values. As with grid search, it selects the hyperparameter that performed the best.
- Bayesian optimization is another approach to hyperparameter tuning. It uses ideas from field of Bayesian statistics to iterate through different hyperparameter values. Each time the Bayesian optimization algorithm evaluates a new hyperparameter value, it gains more information about where it should look for the best hyperparameter value.
- Genetic algorithms are another possible hyperparameter tuning method. These work by going through several generations of hyperparameter values. Within each generation, the fittest (i.e., best-performing) hyperparameter values are slightly mutated (i.e., changed) in order to produce the next generation.
