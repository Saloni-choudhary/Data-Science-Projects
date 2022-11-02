#!/usr/bin/env python
# coding: utf-8

# # Player's Performance Analysis using Python
# 
# ## One of the use cases of data science in sports analytics is analyzing a player's performance . Virat Kohli is one of the most famous cricketers in the world. So in this , we will be analyzing the batting performance of Virat Kohli over the years.
# 

# ## Importing the python libraries and the dataset.

# In[42]:


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("VK.csv")
print(data.head())


# ## Checking for the null values

# In[43]:


print(data.isnull().sum())


# ## This dataset contains matches played by Virat Kohli from 18/08/2008 to 22/01/2017. So let's have a look at the total runs scored by Virat Kohli:

# In[44]:


data["Runs"].sum()


# ##  Now let's have a look at the average runs scored by Virat Kohli:

# In[45]:


data["Runs"].mean()


# ## Now let's have a look at the graph of runs scored by Virat Kohli from 18/08/2008 to 22/01/2017.

# In[46]:


matches = data.index
figure = px.line(data, x=matches, y="Runs", title="Runs Scored by Virat Kohli between 18-08-2008 and 22-01-2017")
figure.show()


# ## We'll now look at the batting positions played by Virat Kohli:

# In[47]:


#data positions
data["Pos"] = data["Pos"].map({1.0: "Batting at 1", 2.0: "Batting at 2", 3.0: "Batting at 3", 4.0: "Batting at 4", 5.0: "Batting at 5", 6.0: "Batting at 6", 7.0: "Batting at 7"})

Pos= data["Pos"].value_counts()
label= Pos.index
counts= Pos.values
colors = ['gold','lightgreen', "pink", "blue", "skyblue", "cyan", "orange"]


fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Number of Matches At Different Batting Positions')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# ## Now let's look at the total runs scored by Virat Kohli at different positions:
# 

# In[48]:


label = data["Pos"]
counts = data["Runs"]
colors = ['gold','lightgreen', "pink", "blue", "skyblue", "cyan", "orange"]

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Runs Scored by Virat Kohli in different Positions')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# ## Now let us look at the number of centuries scored by Virat Kohli while batting in first and second innings:

# In[49]:


centuries = data.query("Runs>=100")

figure = px.bar(centuries, x=centuries["Inns"], y=centuries["Runs"],
               color = centuries["Runs"],
               title="Centuries by Virat Kohli in First Innings Vs. Second Innings")
figure.show()


# ## Dismissals faced by Virat Kohli

# In[50]:


dismissal = data["Dismissal"].value_counts()
label = dismissal.index
counts = dismissal.values
colors = ['gold', 'pink', 'lightgreen','cyan','blue','orange','skyblue']

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Dismissals of Virat Kohli')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# ## Lets have a look against which team Virat Kohli scored the most.

# In[51]:


figure = px.bar(data, x=data["Opposition"], y=data["Runs"], color=data["Runs"],
               title="Most Runs Against Teams")

figure.show()


# # Analyzing Virat Kohli's Strike Rate
# ## For this, I'll create a new dataset of all the matches played by him where his strike rate was more than 120:

# In[52]:


strike_rate = data.query("SR >=120")
print(strike_rate)


# ## Now Let's see whether Virat Kohli plays with high strike rates in First innings or Second innings:

# In[53]:


figure = px.bar(strike_rate, x=strike_rate["Inns"],
               y = strike_rate["SR"],
               color=strike_rate["SR"],
               title="Virat Kohli's High Strike Rate in First Innings Vs. Second Innings")

figure.show()


# ## Relationship between runs scored and sixes played by Virat Kohli:

# In[54]:


figure  = px.scatter(data_frame = data, x="Runs",
                    y="6s", trendline="ols",
                    title="Relationship Between Runs Scored and Sixes")

figure.show()


# ## Relationship between runs scored and fours played by Virat Kohli:

# In[55]:


figure = px.scatter(data_frame = data, x="Runs",
                   y="4s", trendline="ols",
                   title=" Relationship between Runs scored and fours played")

figure.show()


# # Summary
# ## So, this is how the performance of player( here, Virat Kohli) can be analyzed using Python Programming Language. 
# 
