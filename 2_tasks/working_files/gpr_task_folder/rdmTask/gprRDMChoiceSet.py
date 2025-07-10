#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 15:27:39 2022

@author: hayley
"""

"""
create choice set function for risky decision-making task
"""



def rcsRDMChoiceSet():
    
        
    import numpy as np
    import pandas as pd
    import random
    import copy
    #import matplotlib.pyplot as plt
    
    lnslope = -2 # slope of x and y values
    
    nT = 126; # 42 trials per level (not including the extra 5 trials)
    EVlevels = np.arange(5,25+1,10); # levels: 5, 15, 25
    nEVLevels = int((len(EVlevels))); # number of levels, make integer
    nPts = int(nT/nEVLevels); # the number of trials per level, make integer
    
    
    # create the dataframes where we will store the x (safe)   
    evPointsX = pd.DataFrame(np.nan, index=np.arange(nPts), columns=['level5', 'level15', 'level25'])
    
    
    # setting up the "distribution":
    middleTrials = int(nPts*(2/3)); # number of trials that are sampled in the middle (near indifference when rho=1)
    edgeTrials = int((nPts*(1/3))/2); # number of trials that are sampled on the edges (away from indifference; divided by 2 because these trials are split between sides)
  
    #set x-value points to hit along the three levels:
    evPointsX['level5'] = np.concatenate((np.linspace(0,3,edgeTrials),np.linspace(3.1,6.9,middleTrials),np.linspace(7,10,edgeTrials)))
    evPointsX['level15'] = np.concatenate((np.linspace(10,13,edgeTrials),np.linspace(13.1,16.9,middleTrials),np.linspace(17,20,edgeTrials)))
    evPointsX['level25'] = np.concatenate((np.linspace(20,23,edgeTrials),np.linspace(23.1,26.9,middleTrials),np.linspace(27,30,edgeTrials)))

    
    # flip each column upside down  and double the values for our Y (risky gain values)coordinates 
    evPointsY = evPointsX.loc[::-1].reset_index(drop=True)*-lnslope

    
    # add noise by creating a matrix of noise that will be applied to our evPointsX and evPointsY matrices

    # from a uniform distribution spanning 0 from -.5 to .5, pick 2 values, multiply by 10, round to 1 digit and divide by 10 to get 2 decimals
    addNoiseX = pd.DataFrame(np.random.uniform(.5, -.5,size=(nPts,nEVLevels)), index=np.arange(nPts),columns=['level5', 'level15', 'level25'])
    addNoiseX = round(addNoiseX*10,1)/10; # this formats the values so they have two decimals (like monetary values should)
    addNoiseY = addNoiseX*2;

    evPointsXnoise = round(evPointsX + addNoiseX, 2)
    evPointsYnoise = round(evPointsY + addNoiseY, 2)
    
    
    # adding noise may create negative values, make those zero (note that this changes some risky gain value and safe values to zero)
    evPointsXnoise[evPointsXnoise<0] = 0;
    evPointsYnoise[evPointsYnoise<0] = 0;
    
    # Now we use a matrix to make sure we hit all the levels of context (ie. 3 levels of mean expected value=5,15,25)
   
    def resample(x):
        val = x[random.randint(0,len(x)-1)]
        return(val)
    
    n = 0;
    mtxInd=[1,2,3]
    
    while (1):
     n = n + 1;
     mtx = pd.DataFrame(data=1,index=mtxInd,columns=mtxInd);
        
     for r in mtxInd:
         mtx.loc[r,:] = r;
         mtx.loc[r,r] = np.nan;
        
        
     EVs = [];
     evnxt=[];
     for i in range(6):
         if i == 0:
            EVs.append(random.randint(1,3)); #pick a column
         else:
            EVs.append(evnxt); #new column
          
            
         if i < 5:
          if any(~np.isnan(mtx.loc[:,EVs[i]]))==False: # if there are not rows without nan in our current column
             print("breaking")   
             #break

          evnxt= resample(mtx.index[~np.isnan(mtx.loc[:,EVs[i]])].tolist()); # pick next EV from rows where there is not NaN 
          mtx.loc[evnxt,EVs[i]] = np.nan;
        
        
         if all(np.isnan(mtx.loc[:,EVs[0]])):
            mtx.loc[EVs[0],:] = np.nan;
          
        
     if (i == 5):
        break
        
      


    EVs = EVs+EVs; # hit each EV twice
    EVs.append(EVs[0]); # back to the startting level/EV. Now the levels are fully crossed

  # each level of EV will have 2 different run lengths that occur twice (5, 5, 16, 16) for 42 trials
  # we need a 13th run because we will be going back up or down to the first run, so we will add 5 more trials evenly spaced on the final EV level seq(from = 1, to = 42, by = 9) =  c(1,10,19,28,37)
  # the only difference across people for the LAST run is that they will be at different EV levels but run length and index on the EV level will be the same.
  
  
  # translate EVs (1-5) into the actual EVs (5-25)

    realEvs = pd.DataFrame(copy.copy(EVs));


    realEvs[realEvs==3] = EVlevels[2];
    realEvs[realEvs==2] = EVlevels[1];
    realEvs[realEvs==1] = EVlevels[0];
    
  # allocate run lengths
    #rL = [5,16]  
  
    n = 0;
    while (1):
      n = n+1
      
      runLength= [];
     
      d = ([5,16], [5,16],[5,16])
      runmtx = pd.DataFrame(data=d, index=[1,2,3], columns=[1,2])
      for i in range(6): # for the first 6 EVs 
               selectRow = EVs[i]; # row is the first EV
               selectCol = resample(runmtx.columns[~np.isnan(runmtx.loc[selectRow,:])].tolist())
               runLength.append(runmtx.loc[selectRow,selectCol]);
               runmtx.loc[selectRow,selectCol] = np.nan;
      if i == 5:
        break
      
        
    runLength=runLength+runLength;
    runLength.append(5); # extra run is 5 trials
      
    nTri = sum(runLength);
    #nRuns = len(runLength);
  
  
  # TRIAL TIMING FEATURES
  # choice display = 2s, decision window = 2s, isi = .5s, outcome = 1s, iti = c(1s, 1.5s, 2s)
  # possible trial lengths = 6.5s, 7s, 7.5s
  # avg trial length = 7s
  # if we want the task to be 15 minutes long, we can get roughly 128 trials 
  
  
    itiTimes = pd.DataFrame(data=[.75, 1.25, 1.75])
    itiDistTimes =itiTimes**-1.05 
  
  
    itiDistTimes = round(nTri*itiDistTimes/itiDistTimes.sum().tolist(),0); # number of times we see 1, 1.5, 2 (61 40 30)
    ITIs = [];
  
    short = np.repeat(itiTimes.loc[0],itiDistTimes.loc[0])
    medium = np.repeat(itiTimes.loc[1],itiDistTimes.loc[1])
    long = np.repeat(itiTimes.loc[2],itiDistTimes.loc[2])
    ITIs = np.concatenate((short, medium, long))
  
  
    random.shuffle(ITIs); # shuffles ITIs


 # distribute everything to the choice set
    rcsCS = pd.DataFrame(data=np.nan, index=np.arange(nTri), columns =["evLevel", "evInd", "runSize", "isi", "iti", "riskyGain", "riskyLoss", "alternative"])
  
  
    count = 0; # start count at trial 1
    for i in range(len(EVs)):
      rcsCS['evLevel'][count:count+runLength[i]-1] = np.repeat(realEvs.loc[i],runLength[i])
      rcsCS['evInd'][count:count+runLength[i]-1] = np.repeat(EVs[i],runLength[i])
      rcsCS['runSize'][count:count+runLength[i]-1] = np.repeat(runLength[i],runLength[i])
      count = count + runLength[i]; # update the count


  
    rcsCS['isi'][:] = .5
    rcsCS['iti'][:] = ITIs;

# add gains, safe and loss values such that we hit all the possible values for each level of EV given the number of trials in each run
    
    d=[np.arange(nPts),np.arange(nPts),np.arange(nPts)]; # create three rows of points spanning 0-41
    valueInds = pd.DataFrame(data=np.transpose(d), index=np.arange(nPts), columns = [1,2,3]); # create a matrix where each column corresponds to EV level and there are 42 rows (for 42 trials)
  
  
    for n in range(nT):
    
      getCol = rcsCS['evInd'][n]; # column is level of EV for that trial, n
      if getCol == 1:
          selectCol = 'level5'
      elif getCol ==2:
          selectCol = 'level15'
      elif getCol==3:
          selectCol='level25'
    
    
      selectRow = resample(valueInds.index[~np.isnan(valueInds.loc[:,getCol])].tolist())
# select a row
    
    
      rcsCS['riskyGain'][n] = evPointsYnoise[selectCol][selectRow];
      rcsCS['alternative'][n]= evPointsXnoise[selectCol][selectRow];
      rcsCS['riskyLoss'][n] = 0; #gain only task
    
    
    valueInds.loc[selectRow,getCol] = np.nan; # replace with NA so we don't select this index again
    
   # Now add the last 5 trials: evenly spaced on the final EV level seq(from = 1, to = 42, by = 9) =  1 10 19 28 37 (in R, subtract 1 so that it starts at 0)
    last5rowInd= [0,9,18,27,36];
    random.shuffle(last5rowInd)

    
    getCol = EVs[len(EVs)-1]; # column is level of EV for that trial, n
    if getCol == 1:
        selectCol = 'level5'
    elif getCol ==2:
        selectCol = 'level15'
    elif getCol==3:
        selectCol='level25'


    rcsCS['riskyGain'][nT:nTri-1] = evPointsYnoise[selectCol][last5rowInd] #, EVs[len(EVs)-1]]
    rcsCS['alternative'][nT:nTri-1] = evPointsXnoise[selectCol][last5rowInd] #, EVs[len(EVs)-1]]
    rcsCS['riskyLoss'][nT:nTri-1]=0;

# Add attention checks
  # We want to add two trials where risky gain is large and safe is 0 
  # Let's do this for EV levels 15 and 25 
  
  
  # ev level 15 (middle-value context)
  # making boolean series for ev level
    filter1 = rcsCS["evLevel"]==15
  
  # making boolean series for risky gain
    filter2 = rcsCS["riskyGain"]>35
  
    attnCheck15ind = rcsCS.index[filter1 & filter2];   # pull out rows where the filters apply
    rcsCS['alternative'][resample(attnCheck15ind)] = 0; # pick one of those trials and make it zero
  
  # ev level 25 (high-value context)
    filter1 = rcsCS["evLevel"]==25
  
  # making boolean series for risky gain
    filter2 = rcsCS["riskyGain"]>55
  
    attnCheck25ind = rcsCS.index[filter1 & filter2];# pull out rows where the filters apply
    rcsCS['alternative'][resample(attnCheck25ind)] = 0; # pick one of those trials and make it zero
  


    # for testing purposes, plot our choice set to make sure everything worked
    #plt.plot(rcsCS['evLevel'],'o', color="black")
    #plt.plot(rcsCS['riskyGain'],'o', color="black")
    #plt.plot(rcsCS['alternative'],'o', color="black")
    #plt.plot(rcsCS['alternative'],rcsCS['riskyGain'],'o', color="black")


    return rcsCS
