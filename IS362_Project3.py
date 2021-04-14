#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pymysql


# In[35]:


import pandas as pd


# In[36]:


import sqlalchemy
from sqlalchemy import create_engine


# In[37]:


db_connection_str = 'mysql+pymysql://root:IRch1990$@localhost/chinook'


# In[38]:


db_connection = create_engine(db_connection_str)


# In[45]:


df = pd.read_sql('SELECT LastName, FirstName FROM Customer ORDER BY LastName, FirstName', con=db_connection)


# In[41]:


df


# In[ ]:




