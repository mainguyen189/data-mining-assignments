A sampling distribution is obtained by taking a random sample of a certain size multiple times, taking a sample statistic, and plotting the distribution of this sample statistic.

The Central Limit Theorem establishes that the sampling distribution of the mean will be normally distributed (even if the original population was not normally distributed).

A statistic is called an unbiased estimator of a population parameter if the mean of the sampling distribution of the statistic is equal to the value of the statistic for the population. The mean is an unbiased estimator.

We can use the Standard Error of our sample mean distribution in order to calculate probabilities of obtaining a sample with a certain statistic using the CDF.







One-sample t-tests are used for comparing a sample mean to an expected population mean

A one-sample t-test can be implemented in Python using the SciPy ttest_1samp() function

Assumptions of a one-sample t-test include:
- The sample was randomly drawn from the population of interest
- The observations in the sample are independent
- The sample size is large “enough” or the sample data is normally distributed
