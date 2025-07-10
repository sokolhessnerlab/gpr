#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 26 12:20:06 2022

@author: hayley
 - Modification Author: Justin Blake
"""

"""
Primary script for HJRB's Senior Honor's Thesis Project GPR
This script does some set up for the experiment and calls all required scripts to run the risky decision-making and cognitive control tasks
"""

#import os
#os.chdir('/Users/justinblake/Documents/GitHub/gpr/2_tasks/working_files/gpr_task_folder')
#import gprPrimary
#gprPrimary.gprPrimary("xxx", x, x)

def gprPrimary(subID, isReal, computerNumber): # define the function and specify the argument(s)

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
        dirName = ("/Users/justinblake/Documents/GitHub/gpr/2_tasks/working_files/gpr_task_folder/")
        dataDirName = ("/Users/justinblake/Documents/GitHub/gpr/2_tasks/working_files/gpr_task_folder/rdmTask/data/")
    elif computerNumber ==2:
        dirName = ("/Users/shlab/Documents/Github/gpr/task/")
        dataDirName = ("/Users/shlab/Documents/Github/gpr/task/data")
    elif computerNumber ==3:
        dirName = ("/Users/Display/Desktop/Github/gpr/task/") 
        dataDirName = ("/Users/Display/Desktop/gprData/")
    elif computerNumber ==4:
        dirName = ("/Users/sokolhessnerlab/Desktop/Github/gpr/task/")
        dataDirName =("/Users/sokolhessnerlab/Desktop/gprData/")
    
    os.chdir(dirName)

    
    # Import scripts
    from rdmTask.gprRDMmodule import gprRDM # risky decision-making task + condition instructions
   #from cgt_digitSpan import digitSpan_shlab
        
    # r  d condition order from pre-existing text file which determines conditions and color for each round of RDM task
    #conditionDF = pd.read_csv(dirName + "rdmTask/gprConditions.csv", dtype={"subID":"string"}) # specify that subID is a string
    conditionDF = pd.read_csv(dirName + "rdmTask/gprConditions.csv", dtype={"gprID":"string"}) # specify that subID is a string
    
    # reading the csv file above does some weird stuff to the subID column, removing the extra characters:
    #conditionDF.subID = conditionDF["subID"].str.replace("=","")
    #conditionDF.subID = conditionDF["subID"].str.replace('"',"")
    gprIdx = int(subID) % 25
    # determine condition 1 and condition 2 (0=control, 1 = strategy) for participant
    cond1 = conditionDF.cond1.iloc[gprIdx]
    cond2 = conditionDF.cond2.iloc[gprIdx]
    
    # determine condition 1 and condition 2 (0=control, 1 = strategy) for participant
    cond3 = conditionDF.cond3.iloc[gprIdx]
    cond4 = conditionDF.cond4.iloc[gprIdx]
     
    # determine the condition colors (green = 0, purple = 1, blue = 2, orange = 3)
    cond1color = conditionDF.cond1color.iloc[gprIdx]
    cond2color = conditionDF.cond2color.iloc[gprIdx]
    cond3color = conditionDF.cond3color.iloc[gprIdx]
    cond4color = conditionDF.cond4color.iloc[gprIdx]
    

    gprRDM(subID, cond1, cond2, cond3, cond4, cond1color, cond2color, cond3color, cond4color, isReal, dirName, dataDirName)
    
    
    # simple analysis script (checks for missing trials, runs simple glm, scores span tasks, notes whether we keep the data and then adjusts the condition file)

def getNextSubID(writeToFile=False):
    """
    Get the next subject ID from the Subjects file and write it with a timestamp.
    """
    import pandas as pd
    from datetime import datetime
    import os

    subjects_file = "2_tasks/working_files/gpr_task_folder/gprSubjects.csv"

    # Check if file exists, if not create with headers
    if not os.path.exists(subjects_file):
        df = pd.DataFrame(columns=["subID", "timestamp"])
        df.to_csv(subjects_file, index=False)

    conditionDF = pd.read_csv(subjects_file, dtype={"subID": "string"})
    next_subID = conditionDF['subID'].max()  # Get the maximum subID
    if next_subID is None or pd.isna(next_subID):
        next_subID = 0
    next_subID = int(next_subID) + 1  # Increment by 1 for the next participant
    next_subID_str = str(next_subID).zfill(3)  # Zero-padded string

    # Write new subID and timestamp to file if we are writing to file
    if writeToFile:
        timestamp = datetime.now().isoformat()
        with open(subjects_file, 'a') as f:
            f.write(f"{next_subID_str},{timestamp}\n")

    return next_subID_str

def main():
    isTesting = 0 # Set to 0 for testing, 1 for real
    subId = getNextSubID(True if isTesting == 1 else False)  # Get the next subject ID
    computerNumber = 1  # Set the computer number (1 for HB macbook, etc.)
    gprPrimary(subId, isTesting, computerNumber) # call the function with the arguments specified above
    
if __name__ == "__main__":
    main()  # Run the main function when the script is executed
