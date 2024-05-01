#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns


# In[5]:


df_hospitaldischarge=pd.read_excel('Cardiac_Outcomes.xlsx', sheet_name='Hospitalization_Discharge')


# In[6]:


df_hospitaldischarge


# In[7]:


df_CardiacComplications=pd.read_excel('Cardiac_Outcomes.xlsx', sheet_name='CardiacComplications')


# In[8]:


df_CardiacComplications


# In[10]:


df_Responsivenes=pd.read_excel('Cardiac_Outcomes.xlsx', sheet_name='Responsivenes')


# In[11]:


df_Responsivenes


# In[12]:


df_PatientHistory=pd.read_excel('Cardiac_Outcomes.xlsx', sheet_name='PatientHistory')


# In[13]:


df_PatientHistory


# In[15]:


df_Labs=pd.read_excel('Cardiac_Outcomes.xlsx', sheet_name='Labs')


# In[16]:


df_Labs


# In[17]:


df_Demography=pd.read_excel('Cardiac_Outcomes.xlsx', sheet_name='Demography')


# In[18]:


df_Demography


# In[19]:


df_PatientPrecriptions=pd.read_excel('Cardiac_Outcomes.xlsx', sheet_name='Patient_Precriptions')


# In[20]:


df_PatientPrecriptions


# # Question no.65 Which Admission Ward has maximum number of visits scheduled

# In[21]:


df_hospitaldischarge.groupby('admission_ward')['visit_times'].sum()


# # Question no.66 Display total count of patients in each discharge_department based on gender

# In[22]:


df1=df_hospitaldischarge[['discharge_department','inpatient_number']]
df2=df_Demography[['gender','inpatient_number']]


# In[23]:


merge_1=df1.merge(df2,left_on='inpatient_number', right_on='inpatient_number')
merge_1


# In[24]:


merge_1.groupby(['discharge_department','gender'])['inpatient_number'].sum()


# # Question no. 67 How many Unique patients were precribed each type of medication?

# In[25]:


df_PatientPrecriptions.groupby('Drug_name').nunique()


# # Question no. 68 Find 5 patients with the highest Discharge days greater than 20. List their most common outcome

# In[26]:


df1=df_hospitaldischarge[df_hospitaldischarge['dischargeDay']>20]
df2=df1.sort_values(by='dischargeDay', ascending=False).head(5)
df2['outcome_during_hospitalization'].mode()


# # Question 71 Which year had the maximum admissions

# In[27]:


date_column=pd.DatetimeIndex(df_hospitaldischarge['Admission_date'])
#Creating a new column year in df_hospitaldischarge
df_hospitaldischarge['year']=date_column.year
df_hospitaldischarge


# In[28]:


df1=df_hospitaldischarge.groupby('year')['inpatient_number'].max()
df1


# # Question 72 What % of the dataset is male vs female?
# 

# In[29]:


df_patients=df_Demography['inpatient_number'].sum()
df_patients


# In[30]:


df_patients_gender=df_Demography.groupby('gender')['inpatient_number'].sum()
df_patients_gender


# In[31]:


percentage=(df_patients_gender/df_patients)*100
percentage


# # Question no. 73 Which patient in the youngest age category weighs the most?

# In[32]:


#Finding youngest age catogery
df_Demography['ageCat'].min()


# In[33]:


#Filtering the youngest age catgory
df1 = df_Demography[(df_Demography['ageCat'] == '21-29')]
df1


# In[34]:


# Finding the maximum weight of patient within youngest age category
df1['weight'].max()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Question 80 Delete the column age from Q26 iteratively.
# 

# In[ ]:


df_Demography.drop('newlycreated_column_name', axis=1, inplace=True)

