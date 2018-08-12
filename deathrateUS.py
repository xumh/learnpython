
# coding: utf-8

# In[28]:


import csv, numpy
f=open("guns.csv")
data=list(csv.reader(f))
print(data[:6])


# In[29]:


headers=data[0]
data=data[1:]


# In[30]:


years=[each[1] for each in data]
year_counts={}
for each in years:
    if each in year_counts:
        year_counts[each]+=1
    else:
        year_counts[each]=1
print(year_counts)


# In[31]:


import datetime
dates=[]
for each in data:
    date = datetime.datetime(year=int(each[1]), month=int(each[2]), day=1)
    dates.append(date)

dates_counts={}
for each in dates:
    if each in dates_counts:
        dates_counts[each]+=1
    else:
        dates_counts[each]=1

print(dates_counts)


# In[32]:


sex=[each[5] for each in data]
sex_counts={}
for each in sex:
    if each in sex_counts:
        sex_counts[each]+=1
    else:
        sex_counts[each]=1

print(sex_counts)


# In[33]:


race=[each[7] for each in data]
race_counts={}
for each in race:
    if each in race_counts:
        race_counts[each]+=1
    else:
        race_counts[each]=1

print(race_counts)


# In[34]:


f=open("census.csv")
data1=list(csv.reader(f))
print(data1)


# In[35]:


mapping={"Asian/Pacific Islander":15834141, "Black":40250635, "Native American/Native Alaskan":3739506, "Hispanic":44618105, "White":197318956}
race_per_hundredk={}
for key in race_counts:
    race_per_hundredk[key]=race_counts[key]/mapping[key]*100000
    
print(race_per_hundredk)


# In[38]:


intents=[each[3] for each in data]
races=[each[7] for each in data]
homicide_race_counts={}
for i,race in enumerate(races):
    if intents[i]=="Homicide":
        if race not in homicide_race_counts:
            homicide_race_counts[race]=1
        else:
            homicide_race_counts[race]+=1

#print(homicide_race_counts)

race_per_hundredk={}
for key in homicide_race_counts:
    race_per_hundredk[key]=homicide_race_counts[key]/mapping[key]*100000
    
print(race_per_hundredk)


# In[39]:


intents=[each[3] for each in data]
intent_counts={}
for each in intents:
    if each in intent_counts:
        intent_counts[each]+=1
    else:
        intent_counts[each]=1

print(intent_counts)

