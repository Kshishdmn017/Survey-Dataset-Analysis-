#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import matplotlib.pyplot  as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
pd.set_option('display.max_rows', 11251)


# # Load the dataset into a pandas dataframe. Name the veriable as "survey".

# In[2]:


survey = pd.read_csv("E:\SQL\python\projects\survey\Survey Dataset - Technical Interview.csv", encoding= 'unicode_escape')


# In[4]:


survey.dtypes 


# In[5]:


survey.ndim


# In[6]:


survey.T


# # How many samples were collected on each day ?

# In[7]:


survey.collection_date.unique()


# In[8]:


survey.collection_date.nunique()


# In[9]:


survey.collection_date.value_counts(ascending = True)


# In[111]:


survey.groupby('collection_date').collection_date.nunique() #number of unique value 


# # What is proportion of the total respondents were aged less then 45?

# In[11]:


survey.head(2)


# In[13]:


survey['age'].replace({'24ko':24}, inplace =True)


# In[14]:


survey.age.unique()


# In[15]:


survey['age'] = survey.age.astype(int)


# In[16]:


survey.age.dtype


# In[17]:


survey[survey['age'] < 45]


# In[18]:


6399/6867 *100


# ### Create a new column in the dataframe "age_group". this column should contain the age group the respondent belongs to . The age groups are 18-25,25-40,40-55 and 55+. The dataframe should look like this after the column creation: 
#     !![image-2.png](attachment:image-2.png)

# In[20]:


data =survey.copy()


# In[21]:


data.head(2)


# In[22]:


#data.insert(new_column_position(0,1,2,3...),"new_column_name",'new_coulumn value')

data.insert(10,"age_group",survey.age)


# In[23]:


data.head(2)


# In[24]:


data1 = data[(data.age_group >= 18) & (data.age_group < 25)]


# In[25]:


data1.head(2)


# In[26]:


data1.age_group.unique()


# In[27]:


data1['age_group'] = '18-25'


# In[28]:


data1.head(1)


# In[29]:


data2 = data[(data.age_group >= 25) & (data.age_group < 40)]


# In[30]:


data2['age_group'] = '25-40'


# In[31]:


data3 = data[(data.age_group >= 40) & (data.age_group < 55)]
data3['age_group'] = '40-55'


# In[32]:


data4 = data[(data.age_group >= 55)]
data4['age_group'] = '55+'


# In[33]:


data = pd.concat([data1,data2,data3,data4])
pd.concat([data])


# In[34]:


data.tail(4)


# In[35]:


data.age_group.unique()


# ### How many samples were collected for each age group ? Which age found had the most samples ?

# In[36]:


data.age_group.value_counts()


# ### What proporttion of the respondents had opted for the RJD party in both the Vote_Now and the Past_vote questions?

# In[37]:


data.head(3)


# In[38]:


survey.Vote_Now.unique()


# In[39]:


survey.Past_Vote.unique()


# In[40]:


survey[survey['Vote_Now'] == 'RJD']


# In[41]:


survey[survey['Past_Vote'] == 'RJD']


# In[42]:


survey[(survey['Vote_Now'] == 'RJD') & (survey['Past_Vote'] == 'RJD')].shape


# In[43]:


811/6867 * 100


# #### For each day of sample collection , determine the proportion of respondents who were fully satisfied with the performance of the CM. So if there were a total of 1000 samples on day 1 and 300 out of those said they were fully satisfied, then our awnser for that day would be 0.3 

# In[44]:


survey.head(3)


# In[45]:


CM= survey[survey.CM_satisfaction == 'Fully Satisfied']


# In[46]:


CM.shape


# In[47]:


a= CM.collection_date.value_counts()
print(a)


# In[48]:


b = survey.collection_date.value_counts()
print(b)


# In[49]:


a/b * 100 


# #### In a similar fashion create a day-wise proportion of respondents that opted fully dissatisfied with their MLA. Create a line plot of the result with date on x-axis and proportions on the y-axis.

# In[50]:


data.head(2)


# In[51]:


data['MLA_satisfaction'].unique()


# In[53]:


MLA =data[data['MLA_satisfaction'] == 'Fully Dissatisfied']


# In[55]:


c = MLA.collection_date.value_counts()
print(c)


# In[56]:


d = survey.collection_date.value_counts()
print(d)


# In[58]:


e =c/d * 100
print(e)


# In[70]:


type(e)


# In[81]:


g = pd.DataFrame(e)
g


# In[88]:


g.collection_date.plot(kind = 'line', figsize=(20,10));


# ### Create a pivot-table with index as Past_Vote, Column as Vote_Now and cell values as the count of sample 

# In[90]:


survey.pivot_table(index ='Past_Vote', columns ='Vote_Now',aggfunc ='count')


# ### Repeat the above question with the cell values as the sum of "weight".

# In[94]:


survey.pivot_table(index ='Past_Vote', columns ='Vote_Now',values ='weight', aggfunc ='sum')


# ### Create a dataframe by performing a group by over age_group and calculate the count of total samples under each age_group

# In[112]:


df1 = data.groupby('age_group').count()


# In[113]:


df1


# In[102]:


type(df1)


# ### Create a dataframe by performing a group by over age_group and finding the count of total samples for each age_group thet opted for the JD(U) party in Vote_Now.

# In[120]:


df2 = data[data['Vote_Now'] == 'JD(U)'].groupby('age_group').count()
df2


# ### To merge two different df using above two questions!

# In[122]:


pd.merge(df1,df2 , on ='age_group')


# In[ ]:




