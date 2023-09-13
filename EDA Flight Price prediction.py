#!/usr/bin/env python
# coding: utf-8

# ### FEATURES
# The various features of the cleaned dataset are explained below:
# 
# 1) Airline: The name of the airline company is stored in the airline column. It is a categorical feature having 6 different airlines.
# 
# 2) Flight: Flight stores information regarding the plane's flight code. It is a categorical feature.
# 
# 3) Source City: City from which the flight takes off. It is a categorical feature having 6 unique cities.
# 
# 4) Departure Time: This is a derived categorical feature obtained created by grouping time periods into bins. It stores information about the departure time and have 6 unique time labels.
# 
# 5) Stops: A categorical feature with 3 distinct values that stores the number of stops between the source and destination cities.
# 
# 6) Arrival Time: This is a derived categorical feature created by grouping time intervals into bins. It has six distinct time labels and keeps information about the arrival time.
# 
# 7) Destination City: City where the flight will land. It is a categorical feature having 6 unique cities.
# 
# 8) Class: A categorical feature that contains information on seat class; it has two distinct values: Business and Economy.
# 
# 9) Duration: A continuous feature that displays the overall amount of time it takes to travel between cities in hours.
# 
# 10)Days Left: This is a derived characteristic that is calculated by subtracting the trip date by the booking date.
# 
# 11) Price: Target variable stores information of the ticket price.

# In[ ]:


#importing basics libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


df=pd.read_excel('flight_price.xlsx')
df.head()


# In[ ]:


df.tail()


# In[ ]:


## get the basics info about data
df.info()


# In[ ]:


df.describe()


# In[ ]:


df.head()


# In[ ]:


## Feature Engineering
df['Date']=df['Date_of_Journey'].str.split('/').str[0]
df['Month']=df['Date_of_Journey'].str.split('/').str[1]
df['Year']=df['Date_of_Journey'].str.split('/').str[2]


# In[ ]:


df.info()


# In[ ]:


df['Date']=df['Date'].astype(int)
df['Month']=df['Month'].astype(int)
df['Year']=df['Year'].astype(int)


# In[ ]:


df.info()


# In[ ]:


## Drop Date Of Journey

df.drop('Date_of_Journey',axis=1,inplace=True)


# In[ ]:


df.head()


# In[ ]:


df['Arrival_Time']=df['Arrival_Time'].apply(lambda x:x.split(' ')[0])


# In[ ]:


df['Arrival_hour']=df['Arrival_Time'].str.split(':').str[0]
df['Arrival_min']=df['Arrival_Time'].str.split(':').str[1]


# In[ ]:


df.head(2)


# In[ ]:


df['Arrival_hour']=df['Arrival_hour'].astype(int)
df['Arrival_min']=df['Arrival_min'].astype(int)


# In[ ]:


df.drop('Arrival_Time',axis=1,inplace=True)


# In[ ]:


df.head(2)


# In[ ]:


df['Departure_hour']=df['Dep_Time'].str.split(':').str[0]
df['Departure_min']=df['Dep_Time'].str.split(':').str[1]


# In[ ]:


df['Departure_hour']=df['Departure_hour'].astype(int)
df['Departure_min']=df['Departure_min'].astype(int)


# In[ ]:


df.info()


# In[ ]:


df.drop('Dep_Time',axis=1,inplace=True)


# In[ ]:


df.head(2)


# In[ ]:


df['Total_Stops'].unique()


# In[ ]:


df[df['Total_Stops'].isnull()]


# In[ ]:


df['Total_Stops'].mode()


# In[ ]:


df['Total_Stops'].unique()


# In[ ]:


df['Total_Stops']=df['Total_Stops'].map({'non-stop':0,'1 stop':1,'2 stops':2,'3 stops':3,'4 stops':4,np.nan:1})


# In[ ]:


df[df['Total_Stops'].isnull()]


# In[ ]:


df.head(2)


# In[ ]:


df.drop('Route',axis=1,inplace=True)


# In[ ]:


df.head(2)


# In[ ]:


df['Duration'].str.split(' ').str[0].str.split('h').str[0]


# In[ ]:


df['Airline'].unique()


# In[ ]:


df['Source'].unique()


# In[ ]:


df['Additional_Info'].unique()


# In[ ]:


from sklearn.preprocessing import OneHotEncoder


# In[ ]:


encoder=OneHotEncoder()


# In[ ]:


encoder.fit_transform(df[['Airline','Source','Destination']]).toarray()


# In[ ]:


pd.DataFrame(encoder.fit_transform(df[['Airline','Source','Destination']]).toarray(),columns=encoder.get_feature_names_out())


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




