import scipy.stats as stats
import numpy as np

#poisson distribution lambda=7
lam = 7

#probability of observing exactly lambda on a day
print(stats.poisson.pmf(lam, lam))

#probability of observing 4 or fewer on a day
print(stats.poisson.cdf(4, lam))

#probability of observing more than 9 on a day
print(1 - stats.poisson.cdf(9, lam))

#initiate a variable with 356 random values from the possion distribution, mean = lambda
year_defects = stats.poisson.rvs(lam, size = 356)

print(year_defects[0:20])

#check mean = lambda
print(lam*365)
print(sum(year_defects))
print(np.mean(year_defects))

#max value
print(year_defects.max())

#probability of observing max value on a day
1 - stats.poisson.cdf(year_defects.max(), lam)

#how many occurene is in 90th percentile
print(stats.poisson.ppf(0.9, lam))

#check 90th percentile
print(sum(year_defects >= stats.poisson.ppf(0.9, lam))/len(year_defects))
