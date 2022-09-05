SciPy

- one-sample t-test: tval, pval = ttest_1samp(a,b)  
- two-sample t-test: tval, pval = ttest_ind(a,b)
- binominal test: pval = binom_test(a, b, samplesizepercentage, alternative='...')
- one way anova: fstat, pval = f_oneway(a, b, c)
- tukey's range test: pairwise_tukeyhsd(a, b, alpha)
- chi-square: 
table = pd.crosstab(variable_1, variable_2)
chi2, pval, dof, expected = chi2_contingency(table)

One-sample t-tests are used for comparing a sample mean to an expected population mean

Two Sample T-Tests (for an association between a quantitative variable and a binary categorical variable)

ANOVA and Tukey Tests (for an association between a quantitative variable and a non-binary categorical variable)

Chi-Square Tests (for an association between two categorical variables)



