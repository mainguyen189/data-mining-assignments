The “k” refers to the number of clusters (groups) we expect to find in a dataset.

The “Means” refers to the average distance of data to each cluster center, also known as the centroid, which we are trying to minimize.

An iterative approach:
- Place k random centroids for the initial clusters.
- Assign data samples to the nearest centroid.
- Calculate new centroids based on the above-assigned data samples.
- Repeat Steps 2 and 3 until convergence.
- Convergence occurs when points don’t move between clusters and centroids stabilize. This iterative process of updating clusters and centroids is called training.

Once we are happy with our clusters, we can take a new unlabeled datapoint and quickly assign it to the appropriate cluster - inference.
