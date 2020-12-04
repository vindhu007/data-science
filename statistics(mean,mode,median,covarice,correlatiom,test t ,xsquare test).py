#!/usr/bin/env python
# coding: utf-8

# calculating central tendencies using libraries

# In[24]:


import statistics
import numpy as np


# In[21]:


sample=[12,45,32,32,34,65,34,42,17,56,45,34,33,39,35,23,26,27,44,55,66,33,42,21,89,43,14,65,32,45,65,29,39]


# In[30]:


print (statistics.mean(sample))
print (statistics.median(sample))
print (statistics.mode(sample))
print (statistics.stdev(sample))
print (statistics.variance(sample))


# using numpy we cant calculate mode,SD and variance

# In[28]:


print (np.mean(sample))
print (np.median(sample))
##print (np.mode(sample))
##print (np.stdev(sample))
##print (np.variance(sample))


# covariance using numpy

# In[32]:


import numpy as np

A = [45,37,42,35,39]
B = [38,31,26,28,33]
C = [10,15,17,21,12]

data = np.array([A,B,C])

covMatrix = np.cov(data,bias=False)
print (covMatrix)


# In[33]:


import pandas as pd

data = {'A': [45,37,42,35,39],
        'B': [38,31,26,28,33],
        'C': [10,15,17,21,12]
        }

df = pd.DataFrame(data,columns=['A','B','C'])

covMatrix = pd.DataFrame.cov(df)
print (covMatrix)


# correlation coefficeint using numpy and scipy.stats

# In[37]:


import numpy as np
x = np.arange(10, 20)
y = np.array([2, 1, 4, 5, 8, 12, 18, 25, 96, 48])
r = np.corrcoef(x, y)
r


# In[42]:


import numpy as np
import scipy.stats
x = np.arange(10, 20)
y = np.array([2, 1, 4, 5, 8, 12, 18, 25, 96, 48])
r1,p1=scipy.stats.pearsonr(x, y)
r2,p2=scipy.stats.spearmanr(x, y)
r1,p1


# In[48]:


import pandas as pd
x = pd.Series(range(10, 20))
y = pd.Series([2, 1, 4, 5, 8, 12, 18, 25, 96, 48])
x.corr(y)  ##pearson coeff
y.corr(x)
x.corr(y, method='spearman')


# In[83]:


import seaborn as sns


# In[84]:


df=sns.load_dataset('iris')


# In[85]:


df.head()


# In[87]:


df.corr()


# In[88]:


sns.pairplot(df)


# In[49]:


import pandas as pd

data = {'A': [45,37,42,35,39],
        'B': [38,31,26,28,33],
        'C': [10,15,17,21,12]
        }

df = pd.DataFrame(data,columns=['A','B','C'])
print (df.corr())


# distribution formula using python

# In[60]:


from numpy import random

x = random.normal(size=(2, 3))
y = random.binomial(n=10, p=0.5, size=10)
x = random.poisson(lam=2, size=10)
x = random.uniform(size=(2, 3))
x = random.logistic(loc=1, scale=2, size=(2, 3))
x = random.chisquare(df=2, size=(2, 3))


# In[61]:


x = random.normal(loc=1, scale=2, size=(2, 3)) ##mean at 1 and standard deviation of 2
x


# In[62]:


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(size=1000), hist=False)
sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)
sns.distplot(random.poisson(lam=2, size=1000), kde=False)
sns.distplot(random.uniform(size=1000), hist=False)
sns.distplot(random.logistic(size=1000), hist=False)
sns.distplot(random.chisquare(df=1, size=1000), hist=False)

sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')
sns.distplot(random.logistic(size=1000), hist=False, label='logistic')


plt.show()


# one sample t-test

# One sample t-test : The One Sample t Test determines whether the sample mean is statistically different from a known or hypothesised population mean. The One Sample t Test is a parametric test.

# In[15]:


import numpy as np


# In[5]:


ages=[12,45,32,32,34,65,34,42,17,56,45,34,33,39,35,23,26,27,44,55,66,33,42,21,89,43,14,65,32,45,65,29,39]


# In[8]:


ages_mean=np.mean(ages)
ages_mean


# In[9]:


sample_size=10


# In[11]:


age_sample=np.random.choice(ages,sample_size)
age_sample


# In[12]:


from scipy.stats import ttest_1samp


# In[13]:


ttest,pvalue=ttest_1samp(age_sample,40)


# In[14]:


pvalue


# pvalue is greater than 0.05 so we will accepting null hypothiesis

# Two sampled T-test :-The Independent Samples t Test or 2-sample t-test compares the means of two independent groups in order to determine whether there is statistical evidence that the associated population means are significantly different. The Independent Samples t Test is a parametric test. This test is also known as: Independent t Test.

# In[65]:


from scipy.stats import ttest_ind
import numpy as np
ages=[12,45,32,32,34,65,34,42,17,56,45,34,33,39,35,23,26,27,44,55,66,33,42,21,89,43,14,65,32,45,65,29,39]
height=[45,56,34,78,45,23,89,76,45,23,89,23,45,45,33,34,34,23,47,45,39,39,34,36,37,37]

ages_mean = np.mean(ages)
height_mean = np.mean(height)

ages_std = np.std(ages_mean)
ages_std = np.std(height_mean)

ttest,pval = ttest_ind(ages,height)
print("p-value",pval)
if pval <0.05:
  print("we reject null hypothesis")
else:
  print("we accept null hypothesis")


# In[72]:


ttest,pval = ttest_1samp(ages,ages_mean)## one sample test


# In[69]:


pval


# In[79]:


import statistics
from scipy.stats import ttest_ind
import scipy.stats as stats
class_bages=stats.poisson.rvs(loc=18,mu=33,size=60)


# Paired sampled t-test :- The paired sample t-test is also called dependent sample t-test. It’s an uni variate test that tests for a significant difference between 2 related variables. An example of this is if you where to collect the blood pressure for an individual before and after some treatment, condition, or time point.

# In[82]:


import pandas as pd
from scipy import stats
weight1=[10,12,13,14,15,10,12,13,14,15,16,17,18,12,14]
weight2=weight1 + stats.norm.rvs(scale=5,loc=-1.25,size=15)
weight_df=pd.DataFrame({"weight1":np.array(weight1),"weight2":np.array(weight2),"weightdiff":np.array(weight2)-np.array(weight1)})
ttest,pval = stats.ttest_rel(weight1,weight2)
print(pval)
if pval<0.05:
    print("reject null hypothesis")
else:
    print("accept null hypothesis")


# In[ ]:


import pandas as pd
from scipy import stats
df = pd.read_csv("blood_pressure.csv")
df[['bp_before','bp_after']].describe()
ttest,pval = stats.ttest_rel(df['bp_before'], df['bp_after'])
print(pval)
if pval<0.05:
    print("reject null hypothesis")
else:
    print("accept null hypothesis")


# chi-square testing 

# Chi-Square Test- The test is applied when you have two categorical variables from a single population. It is used to determine whether there is a significant association between the two variables.

# In[89]:


import scipy.stats as stats


# In[92]:


import pandas as pd
import numpy as np
import seaborn as sns
data=sns.load_dataset('tips')


# In[93]:


data.head()


# In[95]:


data_table=pd.crosstab(data['sex'],data['smoker'])


# In[96]:


data_table


# In[98]:


observed_values=data_table.values
observed_values


# In[102]:


val=stats.chi2_contingency(data_table)
val


# In[103]:


expected_value=val[3]


# In[107]:


no_of_rows=len(data_table.iloc[0:2,0])
no_of_colums=len(data_table.iloc[0,0:2])
dof=(no_of_rows-1)*(no_of_colums-1)
alpha=0.05


# In[112]:


from scipy.stats import chi2
chi_square=sum([(o-e)**2./e for o,e in zip(observed_values,expected_value)])
chi_square_statistic=chi_square[0]+chi_square[1]

critical_value=chi2.ppf(q=1-alpha,df=dof)
print('critical_value:',critical_value)


# In[115]:



#p-value
p_value=1-chi2.cdf(x=chi_square_statistic,df=dof)
print('p-value:',p_value)
print('Significance level: ',alpha)
print('Degree of Freedom: ',dof)
print('p-value:',p_value)


# In[116]:


if chi_square_statistic>=critical_value:
    print("Reject H0,There is a relationship between 2 categorical variables")
else:
    print("Retain H0,There is no relationship between 2 categorical variables")
    
if p_value<=alpha:
    print("Reject H0,There is a relationship between 2 categorical variables")
else:
    print("Retain H0,There is no relationship between 2 categorical variables")

