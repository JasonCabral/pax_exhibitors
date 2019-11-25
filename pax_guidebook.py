#!/usr/bin/env python
# coding: utf-8

# In[2]:


import urllib.request
from bs4 import BeautifulSoup
import datetime
import pandas as pd


# In[40]:


mainUrl = "https://guidebook.com/guide/166464/list/867382/"
response = urllib.request.urlopen(mainUrl)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')


# In[12]:


links = []
for link in soup.findAll(attrs={'class':'cell-link'}):
    links.append('https://guidebook.com' + link.get('href'))


# In[131]:


data = pd.DataFrame({'name': [], 'booth': [], 'link': [], 'note':[], 'description':[]})


# In[132]:


for i in links:
#     subUrl = i
    subResponse = urllib.request.urlopen(i)
    subHtml = subResponse.read()
    subSoup = BeautifulSoup(subHtml, 'html.parser')
    name = subSoup.findAll(attrs={'class':'item header'})[0].find('h1').get_text()
    note = subSoup.findAll(attrs={'class':'item header'})[0].find('label').get_text()
    booth = subSoup.findAll(attrs={'class':'header-underbar'})[0].find('span').get_text()
    link = ''
    description = ''
    if subSoup.findAll(attrs={'class':'description'})[0].a:
        link = subSoup.findAll(attrs={'class':'description'})[0].a.get('href')
    if subSoup.findAll(attrs={'class':'description'})[0].p:
        description = subSoup.findAll(attrs={'class':'description'})[0].p.get_text()
    data = data.append({'name': name, 'booth': booth, 'link': link, 'note': note, 'description': description}, 
                       ignore_index=True)

    


# In[134]:


data


# In[135]:


data.to_csv("pax_unplugged_2019_exhibitors.csv")


# In[ ]:




