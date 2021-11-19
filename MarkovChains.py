#!/usr/bin/env python
# coding: utf-8

# # <font color='#fd79a8'> Markov Chains

# #### In this page you can find an example to understand markov chains.
# #### Let's see how to predict the next state using Markov Chain, based on current state:

# In[2]:


import numpy as np
import random as rm


# In[3]:


# The statespace
states = ["Sleep","Netflix","Gym"]

# Possible sequences of events
transition = [["SS","SG","SN"],["GS","GG","GN"],["NS","NG","NN"]]

# Probabilities matrix (transition matrix)
ProbabilityMatrix = [[0.1,0.7,0.2],[0.6,0.1,0.3],[0.1,0.7,0.2]]


# In[4]:


def predict_state(days):
    # Choose the starting state
    activityToday = "Netflix"
    print("Start state: " + activityToday)
    #starting with the current state only 
    activityList = [activityToday]
    i = 0
    # To calculate the probability of the activity she would do, based on current state
    prob = 1
    while i != days:
        if activityToday == "Sleep":
            change = np.random.choice(transition[0],replace=True,p=ProbabilityMatrix[0])
            if change == "SS":
                prob = prob * 0.1
                activityList.append("Sleep")
                pass
            elif change == "SG":
                prob = prob * 0.7
                activityToday = "Gym"
                activityList.append("Gym")
            else:
                prob = prob * 0.2
                activityToday = "Netflix"
                activityList.append("Netflix")
        elif activityToday == "Gym":
            change = np.random.choice(transition[1],replace=True,p=ProbabilityMatrix[1])
            if change == "GG":
                prob = prob * 0.1
                activityList.append("Gym")
                pass
            elif change == "GS":
                prob = prob * 0.6
                activityToday = "Sleep"
                activityList.append("Sleep")
            else:
                prob = prob * 0.3
                activityToday = "Netflix"
                activityList.append("Netflix")
        elif activityToday == "Netflix":
            change = np.random.choice(transition[2],replace=True,p=ProbabilityMatrix[2])
            if change == "NN":
                prob = prob * 0.2
                activityList.append("Netflix")
                pass
            elif change == "NS":
                prob = prob * 0.1
                activityToday = "Sleep"
                activityList.append("Sleep")
            else:
                prob = prob * 0.7
                activityToday = "Gym"
                activityList.append("Gym")
        i += 1  
    print("Possible states: " + str(activityList))
    print("End state after "+ str(days) + " days: " + activityToday)
    print("Probability of the possible sequence of states: " + str(prob))

# Function that forecasts the possible state for the next 2 days


# ### Prediction for the first day:

# In[5]:


predict_state(1)


# ### Prediction for the 10th day:

# In[6]:


predict_state(10)


# Thanks!
# 
# Source: https://www.udemy.com/course/nidia-natural-language-processing-deep-learning-zero-to-hero/

# In[ ]:




