#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 27 11:57:58 2022

@author: hayley
"""

"""
Randomly set the condition order that participants will be assigned to.
There will be 120 participants and 4 possible orders (control-control, control-strategy, strategy-control, strategy-strategy).
"""


 # condition order codes:
     # 1 = control-control
     # 2 = control-strategy
     # 3 = strategy-control
     # 4 = strategy-strategy
     
 # color order codes:
     # 1 = green - purple
     # 2 = purple - green
     

# import modules
import random, numpy as np, pandas as pd, copy



# set up variables
n=120 # number of participants
condCodes = 1,2,3,4 #conditions
colorCodes = 1,2 # colors (green or purple)
nCond = n/len(condCodes) # number of subs per condition, 
nColor = n/len(colorCodes) # number of subs per color order 

orderList = np.repeat(condCodes, nCond); # create list with 0,1,2,3 repeated 30 times each
random.shuffle(orderList); #shuffle the order

# do the same for the color combinations
colorOrderList = np.repeat(colorCodes, nColor)
random.shuffle(colorOrderList); #shuffle the order

subIDlist = np.array([i for i in range(1,121)]); # subIds from 1-120


# make columns for condition for round1 1 and round 2 of gambling task
# where 0 = control condition
# where 1 = strategy condition

# copying the orderlist for cond1 and cond2 variables
cond1 = copy.copy(orderList); 
cond2 = copy.copy(orderList);


# some conditional statements
# control condition first
cond1[[i for i, j in enumerate(cond1) if j == 1]]= 0
cond1[[i for i, j in enumerate(cond1) if j == 2]]= 0

# strategy condition first
cond1[[i for i, j in enumerate(cond1) if j == 3]]= 1
cond1[[i for i, j in enumerate(cond1) if j == 4]]= 1


# control condition second
cond2[[i for i, j in enumerate(cond2) if j == 1]]= 0
cond2[[i for i, j in enumerate(cond2) if j == 3]]= 0

# strategy condition second
cond2[[i for i, j in enumerate(cond2) if j == 2]]= 1
cond2[[i for i, j in enumerate(cond2) if j == 4]]= 1



# make columns for color order for round1 1 and round 2 of gambling task
# where 0 = green
# where 1 = purple

cond1color = copy.copy(colorOrderList)
cond2color = copy.copy(colorOrderList)

cond1color[[i for i, j in enumerate(cond1color) if j == 1]]= 0 # green for round 1
cond1color[[i for i, j in enumerate(cond1color) if j == 2]]= 1 # purple for round 1


cond2color[[i for i, j in enumerate(cond2color) if j == 2]]= 0 # green for round 2 (don't need to change 1 because that already means purple is second)


data = {
  "condCode": orderList,
  "subID": subIDlist,
  "cond1": cond1,
  "cond2": cond2,
  "cond1color": cond1color,
  "cond2color": cond2color
}

#load data into a DataFrame object:
conditionDF = pd.DataFrame(data)


# change the subIDs to have leading zeroes to be consistent with the rest of the study, e.g. 001
conditionDF['subID'] = conditionDF['subID'].astype(str); # convert subIDs to strings

for i in range(len(conditionDF.subID)):
    if i<9: # remember that python starts indexing at 0
        conditionDF.subID[i] = "00" + conditionDF.subID[i]
    elif i >=9 and i <99:
        conditionDF.subID[i] = "0" + conditionDF.subID[i]

conditionDF.subID = conditionDF.subID.apply('="{}"'.format); # preserve leading zeroes

conditionDF.to_csv("rcsConditions.csv", index=False) # save the csv file
