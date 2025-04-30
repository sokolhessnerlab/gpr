#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 26 12:20:06 2022

@author: hayley
"""

"""
Primary script for HRB's dissertation project RCS
This script does some set up for the experiment and calls all required scripts to run the risky decision-making and cognitive control tasks
"""

    

def rcsPrimary(subID, isReal, computerNumber, taskSet): # define the function and specify the argument(s)

    #isReal = 0 for testing, 1 for real
    # computer numbers:
            # 1 - HB macbook
            # 2 - mahimahi
            # 3 - tofu
            # 4 - goulash
            
    #taskSet:
        # 1: do all
        # 2: do ospan and symspan only
        # 1: do symspan only
    
    # let us know things are starting...
    print('starting study for participant', subID)    

    
    #import modules
    import os
    import pandas as pd
    #import sys

    # set working directory
    if computerNumber ==1:
        dirName = ("/Users/hayley/Documents/Github/rcs/task/")
        dataDirName = ("/Users/hayley/Documents/Github/rcs/task/data")
    elif computerNumber ==2:
        dirName = ("/Users/shlab/Documents/Github/rcs/task/")
        dataDirName = ("/Users/shlab/Documents/Github/rcs/task/data")
    elif computerNumber ==3:
        dirName = ("/Users/Display/Desktop/Github/rcs/task/")
        dataDirName = ("/Users/Display/Desktop/rcsData/")
    elif computerNumber ==4:
        dirName = ("/Users/sokolhessnerlab/Desktop/Github/rcs/task/")
        dataDirName =("/Users/sokolhessnerlab/Desktop/rcsData/")
    
    
    
    os.chdir(dirName)


    
    # Import scripts

    from rdmTask.rcsRDMmodule import rcsRDM # risky decision-making task + condition instructions
    from symspan.symSpanTaskModule import symSpanTask
    from ospan.ospanTaskModule import ospanTask
    
    # read condition order from pre-existing text file which determines conditions and color for each round of RDM task
    #conditionDF = pd.read_csv(dirName + "rdmTask/rcsConditions.csv", dtype={"subID":"string"}) # specify that subID is a string
    conditionDF = pd.read_csv(dirName + "rdmTask/rcsConditionsUpdated_Winter.csv", dtype={"subID":"string"}) # specify that subID is a string
    
    # reading the csv file above does some weird stuff to the subID column, removing the extra characters:
    #conditionDF.subID = conditionDF["subID"].str.replace("=","")
    #conditionDF.subID = conditionDF["subID"].str.replace('"',"")
    
    # determine condition 1 and condition 2 (0=control, 1 = strategy) for participant
    cond1 = conditionDF.cond1[conditionDF.subID == subID]
    cond1 = cond1.iat[0] # just save the integer, not the extra info like dtype and Name
    cond2 = conditionDF.cond2[conditionDF.subID == subID]
    cond2 = cond2.iat[0] # just save the integer, not the extra info like dtype and Name
     
    # determine the condition colors (green = 0 or purple = 1)
    cond1color = conditionDF.cond1color[conditionDF.subID == subID]
    cond1color = cond1color.iat[0] # just save the integer, not the extra info like dtype and Name
    cond2color = conditionDF.cond2color[conditionDF.subID == subID]
    cond2color = cond2color.iat[0] # just save the integer, not the extra info like dtype and Name
    
    
    
    if taskSet ==1:
        
        # risky decision-making task (input arguments determined above)
        rcsRDM(subID, cond1, cond2, cond1color, cond2color, isReal, dirName, dataDirName)
        
        # ospan instructions + instructions quiz + practice + task
        ospanTask(subID, isReal,dirName, dataDirName)
        
        # symspan instructions + instructions quiz + practice + task
        symSpanTask(subID, isReal,dirName, dataDirName)
        
    elif taskSet==2:
        
        ospanTask(subID, isReal,dirName, dataDirName)

        symSpanTask(subID, isReal,dirName, dataDirName)
        
    elif taskSet==3:
        
        symSpanTask(subID, isReal,dirName, dataDirName)
    
    
    # simple analysis script (checks for missing trials, runs simple glm, scores span tasks, notes whether we keep the data and then adjusts the condition file)
    
    
    
    
    
    
