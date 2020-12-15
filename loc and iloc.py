#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing pandas and numpy
import pandas as pd
import numpy as np

# crete a sample dataframe
data = pd.DataFrame({
    'age' :     [ 10, 22, 13, 21, 12, 11, 17],
    'section' : [ 'A', 'B', 'C', 'B', 'B', 'A', 'A'],
    'city' :    [ 'Gurgaon', 'Delhi', 'Mumbai', 'Delhi', 'Mumbai', 'Delhi', 'Mumbai'],
    'gender' :  [ 'M', 'F', 'F', 'M', 'M', 'M', 'F'],
    'favourite_color' : [ 'red', np.NAN, 'yellow', np.NAN, 'black', 'green', 'red']
})

# view the data
data


# loc is label-based, which means that we have to specify the name of the rows and columns that we need to filter out.

# loc is inclusive and iloc is exlusive of the number given

# we need to give rows and columns for loc and iloc but explicitly all columns are taken ie,[0:4] means all rows from 0 to 4 and all columns,internally it is actually [0:4,:]

# ix is a combination of loc and iloc. iloc is called integer based and loc is called label based.

# if there a cateogorical indexes then we can give the name or just the number in ix

# when we have a string column and we are giving by numbers it will take as postions and if we are having string index and giving as integer it will take as lables when labels are there it is inclusive on both sides.

# In[10]:


data.loc[0,['age','section']]


# In[11]:


data.loc[0]


# In[12]:


data.loc[data.age>=15]


# In[16]:


data.loc[(data.age>=15) & (data.gender=='M')]


# In[17]:


data.loc[0:3]


# In[19]:


data.loc[(data.age>=15),['age','city']]


# UPDATING USING LOC

# In[22]:


data.head(5)


# In[24]:


data.loc[0,['section']]='G'


# In[26]:


data.head(1)


# In[29]:


data.loc[(data.age>=15),['section']]='V'


# In[30]:


data


# In[31]:


data.loc[(data.age>=15),['section','city']]=['A','Pune']


# In[32]:


data


# In[36]:


data.iloc[0:2]


# In[37]:


data.loc[0:2]


# In[44]:


data.iloc[[0,2],[1,3]]


# In[46]:


import seaborn as sns


# In[47]:


df=sns.load_dataset('iris')


# In[48]:


df.head(5)


# In[49]:


df.loc[0,:]


# In[53]:


df.loc[0:3,'sepal_length':'petal_width']


# In[60]:


df[df.sepal_length==5.1]


# In[58]:


df.loc[df.sepal_length==5.1]


# In[ ]:




