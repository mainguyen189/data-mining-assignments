SciPy:
- one-sample t-test: tval, pval = ttest_1samp(a,b)
- two-sample t-test: tval, pval = ttest_ind(a,b)
- binomial test: pval = binom_test(a, b, samplesizepercentage, alternative='...')
- one way anova: fstat, pval = f_oneway(a, b, c)
- tukey's range test: pairwise_tukeyhsd(a, b, alpha)
- chi-square: table = pd.crosstab(variable_1, variable_2) chi2, pval, dof, expected = chi2_contingency(table)

One-sample t-tests are used for comparing a sample mean to an expected population mean

Two Sample T-Tests (for an association between a quantitative variable and a binary categorical variable)

Binomial test for binary data and want to compare a sample proportion/frequency to an underlying probability (population value)

ANOVA and Tukey Tests (for an association between a quantitative variable and a non-binary categorical variable). After you have run an ANOVA and found significant results, then you can run Tukey’s HSD to find out which specific groups’s means (compared with each other) are different. The test compares all possible pairs of means.

Chi-Square Tests (for an association between two categorical variables)

---------------------------------------------------------------------------------------------------------
more comprehensive

#Test 
- preceding steps
- Relationship between/What for

Spearman rank correlation coefficient
- Shapiro-Wilk Normality test 
- All 


2 sample t-test
- Fligner-Killeen test variance equal/unequal
- one categorical variable (2 levels) and one continuous (interval) variable

X-square contingency table (interdependence test) 
- Categorical variable and categorical variable


One-way ANOVA
- Equal variance across groups: Flinger-Killen test of homogeneity of variance (violated, #2 hold → unequal-variance version of F-test)
- Each population is normally distributed: Shapiro-Wilk test each group (violated → alt=Kruskal-Wallis Rank Sum Test)
- one categorical variable (>2 levels) and one continuous (interval) variable
- posthoc 


Two-factor ANOVA
- Two categorical variable (and their interaction) and one continuous variable


Linear regression
- Continuous variables can be directly included in regression analysis.
- Categorical variables must be converted into dummy variables.


Residual Analysis 
- Normally distributed: Shapiro-Wilk normality test of the residuals
- Test of constant variance: Breusch-Pagan Test
- After regression to validate model

Multicollinearity: detect=Variance inflation factors(VIFs)
- After regression to make sure no inflated standard error & instability in model


Non-linearity and interaction (usually just quadratic)
- Numeric variable and numeric variable
- Or
- Categorical and categorical variable

