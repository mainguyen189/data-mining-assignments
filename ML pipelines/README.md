Pipelines help make concise, reproducible, code by combining steps of transformers and/or a final estimator.

- Intermediate steps of a pipeline must have both the .fit() and .transform() methods. This includes preprocessing, imputation, feature selection, dimension reduction.
- The final step of a pipeline must have the .fit() method – this can include a transformer or an estimator/model.
- If the pipeline is meant to only transform your data by combining preprocessing and data cleaning steps, then each step in the pipeline will be a transformer. If your pipeline will also include a model (a final estimation or prediction step), then the last step must be an estimator.
- Once the steps of a pipeline are defined, it can be used like an other transformer/estimator by calling fit, transform, and/or predict methods. Similarly, it can be used in place of an estimator in a hyperparameter grid search.
