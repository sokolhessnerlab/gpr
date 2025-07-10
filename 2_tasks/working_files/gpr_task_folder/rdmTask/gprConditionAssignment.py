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
     # 1 = low-low
     # 2 = low-high
     # 3 = high-low
     # 4 = high-high
     
 # color order codes:
     # 1 = green 
     # 2 = purple 
     # 3 = blue
     # 4 = orange
     

# import modules
import random, numpy as np, pandas as pd, copy
from itertools import permutations




# set up variables
condCodes = [0,1,2,3] #conditions

# Generate all permutations of condCodes (length 4)
perms = list(permutations(condCodes, 4))

# Create a DataFrame where each row is [cond1, cond2, cond3, cond4]
# Repeat permutations to reach 120 participants
orderList = [i+1 for i in range(24)]  # not used as condCode, but kept for compatibility
subIDlist = [str(i+1).zfill(3) for i in range(24)]  # gprID with leading zeros

# Repeat perms to fill 120 rows
repeated_perms = perms * (24 // len(perms)) + perms[:24 % len(perms)]
cond1, cond2, cond3, cond4 = zip(*repeated_perms)

data = {
    "gprID": subIDlist,
    "cond1": cond1,
    "cond2": cond2,
    "cond3": cond3,
    "cond4": cond4,
    "cond1color": cond1,
    "cond2color": cond2,
    "cond3color": cond3,
    "cond4color": cond4,
}

#load data into a DataFrame object:
conditionDF = pd.DataFrame(data)

conditionDF.to_csv("2_tasks/working_files/rcs_task_folder/rdmTask/rcsConditions.csv", index=False) # save the csv file
