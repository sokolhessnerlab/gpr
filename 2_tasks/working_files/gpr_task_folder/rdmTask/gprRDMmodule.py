#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 14:26:15 2022

@author: hayley
Modified Date : June 8, 2025
     - Modification Authors: Denver Persinger, Justin Blake
"""


"""
Risky decision-making for HRB dissertation project: Risk, context and strategy. 
"""


# notes: the screen dimensions are going to shift when we put on lab computer, so will the stimuli

#import os
#os.chdir('/Users/justinblake/Documents/GitHub/gpr/2_tasks/working_files/gpr_task_folder')
#import gprPrimary
#gprPrimary.gprPrimary("xxx", x, x)

def gprRDM(subID, cond1, cond2, cond3, cond4, cond1color, cond2color, cond3color, cond4color, isReal, dirName, dataDirName):
    
    
    #subID='001'
    #cond1 = 0
    #cond2 = 1
    #cond1color = 0
    #cond2color = 1
    #isReal (1 = yes, 0 = testing)
    
    #try:   
    
    # Import modules we need
    import random, time, os
    import pandas as pd
    from psychopy import visual, core, event, monitors
    import numpy as np
    import sys
    
    # change directory
    #os.chdir('/Users/hayley/Documents/Github/gpr/rdmTask') # hb mac
    #os.chdir('/Users/shlab/Documents/Github/gpr/task/rdmTask') # mahimahi
    #os.chdir('/Users/Display/Desktop/Github/gpr/rdmTask') # tofu
    os.chdir(dirName + os.sep + 'rdmTask')
    
    
    #dataDirectoryPath = '/Users/shlab/Documents/Github/gpr/task/data/'
    #dataDirectoryPath = dirName + 'data/'
    dataDirectoryPath = dataDirName + os.sep + "rdmData"

    
    # Import the choice set function
    #from gprRDMChoiceSet import *
    sys.path.append(os.path.dirname(__file__))
    sys.path.append(os.path.join(os.path.dirname(__file__), 'rdmTask'))
    import gprRDMChoiceSet

    # df = pandas.read_csv(dirName + "rdmTask/" + 'gprRDMstatic.csv', dtype={"percentile":"int"}) 

    staticDF = pd.read_csv(dirName + os.sep + "rdmTask" + os.sep + "gprRDMstatic.csv") 

    # Define rounds of risky decision-making task
    RDMrounds=4; 
    
    # Store conditions in one structure 
    cond = [cond1, cond2, cond3, cond4] #(0= control, 1 = strategy, 2=something, 3=something else)
    colorOrder = [cond1color, cond2color, cond3color, cond4color] #(green = 0, purple = 1, blue = 2, orange = 3)
    #colorOrder = [int(cond1color), int(cond2color), int(cond3color), int(cond4color)]
#    import math
#    colorOrder = [int(c) for c in [cond1color, cond2color, cond3color, cond4color] if not math.isnan(c)]
#    index = colorOrder[0]
#    if 0 <= index < len(colors):
#        curr_color = colors[index]
#    else:
#        raise IndexError(f"Index {index} is out of range for colors list of length {len(colors)}")

    colors = [[0,.6,0], [.5,0,.5], [0,.7,.9], [.9,.6,0]] # green, purple, blue, orange
                
    curr_color = colors[colorOrder[0]]
    # Set up the experimental parameters that are consistent across task rounds:
    
    # Screen dimensions and drawing stuff
    #scrnsize= [800,800] #how large the screen will be
    scrnsize=[1280,1024] # CORRECT DIMENSIONS FOR REAL TASK
    #scrnsize = [1024,819.2] # 80% of correct size for mac laptop --> MAC LAPTOP CORRECT SIZE
    center = [0,100]
    centerR = [scrnsize[0]/4,100]
    centerL = [scrnsize[0]/-4,100]
    topR = [scrnsize[0]/10, scrnsize[1]/2]
    topL = [scrnsize[0]/-10, scrnsize[1]/2]
    radius = scrnsize[0]/5.5
    rectHeight = radius +2 #rectangle used to cover up half the circle when outcome is gain or loss
    rectWidth = radius*2+2
    textHeight = 40
    moneyTextHeight= textHeight*2
    wrap = scrnsize[0]*.9 # text wrapping
    
    # earned bonus through all tasks 
    earned_bonus = 0
    
    # BONUS values are represented as a dollar amount
    LOW_BONUS = 25
    HIGH_BONUS = 100
    
    # GOAL is represented as a percentile amount of the amount to hit, the dollar amount is calculatred from CSV data from that percentile
    LOW_GOAL = 10
    HIGH_GOAL = 60

    # Practice goal & bonus definition
    goalPract = 75.20
    bonusPract = 5
    
    df = pd.read_csv(dirName + os.sep + "rdmTask" + os.sep + 'gpr_percentiles.csv', dtype={"percentile":"int"}) 
    LOW_GOAL_AMOUNT = df.iloc[LOW_GOAL-1]['earnings'] 
    HIGH_GOAL_AMOUNT = df.iloc[HIGH_GOAL-1]['earnings']
    
    condition_levels = [(LOW_BONUS, LOW_GOAL_AMOUNT), (LOW_BONUS, HIGH_GOAL_AMOUNT), (HIGH_BONUS, LOW_GOAL_AMOUNT), (HIGH_BONUS, HIGH_GOAL_AMOUNT)]
    
    if isReal == 1:
        nT = 50
        nPract = 5
    else:    
        nT = 2 #for testing purposes
        nPract = 2

    all_round_earnings = [0,0,0,0]
    all_round_bonuses = [0,0,0,0]
    
    #Locations for drawing line and dollar amounts:
    
    lnGamL =[centerL[0]-radius-2, centerL[0]+radius+2] #x start and end points for line when gamble is on the left
    lnGamR = [centerR[0]-radius-2, centerR[0]+radius+2] # x start and end points for line when gamble is on the right
    
    gainGamL = [centerL[0], centerL[1]+(radius*.45)] #position of gain amount when gamble on the left
    gainGamR = [centerR[0], centerR[1]+(radius*.45)] #position of gain amount when gamble on the right
    
    lossGamL= [centerL[0], centerL[1]-(radius*.45)] #position of loss amount when gamble on the left
    lossGamR= [centerR[0], centerR[1]-(radius*.45)] #position of loss amount when gamble on the right
    
    altGamL = [centerR[0], 100] #position of safe amount when gamble on the left
    altGamR = [centerL[0], 100] #position of safe amount when gamble on the right
    
    # Timing stuff
    stimTime = 2
    choiceTime = 2 # time to make a choice after the keys are displayed again
    outcomeTime = 1
    isi = .5

    # Set Up the connection between PsychoPy and Biopac
#    from psychopy.parallel import ParallelPort
#    port = ParallelPort(address = 0xD010)
#    port.setData(0) # zeros it out in case it's not
#    
    # random iti time of 3 or 3.5 sec for each of the trials in the static and dynamic
    def shuffle(array):
        currentIndex = len(array)
        while currentIndex != 0:
            randomIndex = random.randint(0, currentIndex - 1)
            currentIndex -= 1
            array[currentIndex], array[randomIndex] = array[randomIndex], array[currentIndex]

    # Set up the window
    win = visual.Window(
        size=scrnsize,
        units="pix",
        fullscr= True, #For FULLSCREEN, type True, for WINDOW type False
        color=[-1, -1, -1], #black screen
        screen=1 # on second screen
    )
    
    
    # set up stimuli to create the color borders
    blackBox = visual.Rect(
        win,
        width=scrnsize[0]*.95, 
        height=scrnsize[1]*.95, 
        units='pix', 
        pos=[0,0], 
        fillColor='black'
    )
    
    borderBox = visual.Rect(
        win, 
        width=scrnsize[0], 
        height=scrnsize[1], 
        units='pix', 
        pos=[0,0], 
        fillColor=curr_color #green
    )
    
    #PRACTICE SEQUENCE
    pracBorderBox = visual.Rect(
        win,
        width=scrnsize[0],
        height=scrnsize[1],
        units='pix',
        pos = [0,0],
        fillColor='white'
    )
    
    # Prepare instructions and other task stimuli
    forcedInstrWaitTime = 1.5 # participants can't moved forward during instructions until 1.5s have passed

    mes2 = visual.TextStim(
        win, 
        text='Waiting for experimenter', 
        pos = (0,0),
        color=[1,1,1], 
        height =40
    )
    
    inst1 = visual.TextStim(
        win, 
        text="As discussed, in this task you will choose between a gamble and a guaranteed alternative. \n\n\n\nPress 'V' to choose the left option and 'N' to choose the right option.", 
        pos = (0,0),
        color=[1,1,1],
        height = textHeight,
        wrapWidth = wrap, 
        alignText="left"
    )
    
    inst2 = visual.TextStim(
        win, 
        text="Next up are 5 practice trials. \n\nDo you have any questions for the experimenter? \n\nPlease ask the experimenter now.", 
        pos = (0,0),
        color=[1,1,1],
        height = textHeight,
        wrapWidth = wrap,
        alignText="left"
    )
    
    inst3 = visual.TextStim(
        win, 
        text="In this round, your goal is $%.2f. \n\nYour bonus in this round is $%.2f. \n\nTake a moment if you need before beginning the practice. \n\n*REMEMBER, this practice round DOES NOT count toward any actual bonuses. It is meant for explanation and practice purposes ONLY.* \n\nPress 'V' or 'N' when you are ready to begin." % (goalPract, bonusPract), 
        pos = (0,0),
        color=[1,1,1],
        height = textHeight,
        wrapWidth = wrap,
        alignText="left"
    )
    
    postPrac = visual.TextStim(
        win, 
        text="Practice complete! \n\nPlease let the experimenter know you are finished.", 
        pos = (0,0),
        color=[1,1,1],
        height = textHeight,
        wrapWidth = wrap,
        alignText="left"
    )
    
    explainGPRRounds1 = visual.TextStim(
        win,
        text = "Today you will be completing four (4) rounds of the task. \n\nThese rounds are completely independent. \n\nEach round will be marked with a different color - purple, green, blue, or yellow - not necessarily in that order. \n\nEach round will also have different goals and bonuses associated with them. These goals and bonuses will be explained prior to each round. \n\n\nPress 'space' to continue.",
        pos = (0,0),
        color = [1,1,1],
        height = textHeight,
        wrapWidth = wrap,
        alignText = "left"
    )

    readyForRound1 = visual.TextStim(
        win,
        text='Are you ready for ROUND 1 of the task?\n\n\n\nPress ‘space’ to continue.',
        pos = (0,0),
        color=[1,1,1],
        height=textHeight,
        wrapWidth=wrap,
        alignText="left"
    )

    postRoundCheck = visual.TextStim(
        win,
        text="Moving ahead to the next round, do your best to let the outcomes of the previous round go! \n\nFocus instead on the NEW GOAL and BONUS. Rounds are independent from one another, making each round a NEW START. \n\nThe outcomes of any given round have NO EFFECT on subsequent rounds. \n\nBefore advancing, take a moment to get ready if you need, \n\nand press 'space' when you're ready to continue.",
        pos = (0,0),
        color=[1,1,1],
        height=textHeight,
        wrapWidth=wrap,
        alignText="left"
    )               
    
    readyForRound2 = visual.TextStim(
        win,
        text='Are you ready for ROUND 2 of the task?\n\n\n\nPress ‘space’ to continue.',
        pos = (0,0),
        color=[1,1,1],
        height=textHeight,
        wrapWidth=wrap,
        alignText="left"
    )

    readyForRound3 = visual.TextStim(
        win,
        text='Are you ready for ROUND 3 of the task?\n\n\n\nPress ‘space’ to continue.',
        pos = (0,0),
        color=[1,1,1],
        height=textHeight,
        wrapWidth=wrap,
        alignText="left"
    )

    readyForRound4 = visual.TextStim(
        win,
        text='Are you ready for ROUND 4 of the task?\n\n\n\nPress ‘space’ to continue.',
        pos = (0,0),
        color=[1,1,1],
        height=textHeight,
        wrapWidth=wrap,
        alignText="left"
    )

    prepForConditionRound1GPR = visual.TextStim(
        win,
        text = "If you have any questions, please ask the experimenter now. \n\nWhen you are ready, you may press 'space' to continue.",
        pos = (0,0),
        color = [1,1,1],
        height = textHeight,
        wrapWidth = wrap,
        alignText = "left"
    )
    
    # Call experimenter
    callExperimenter = visual.TextStim(
        win,
        text="Please press the white button to call the experimenter back into the room to continue.",
        pos = (0,0),
        color="white",
        height = textHeight,
        wrapWidth=wrap,
        alignText="left"
    )
    
    # CONTROL INSTRUCTIONS (FIRST TIME AROUND)
    controlInstGPR = visual.TextStim(
        win,
        pos = (0,0),
        color=[1,1,1],
        height=textHeight,
        wrapWidth=wrap,
        alignText="left"
    )
    
    # screen count for instructions
    instructCount = visual.TextStim(
        win,
        pos =[scrnsize[1]*.95,-360],
        color=[1,1,1],
        height=textHeight/2,
        wrapWidth=wrap,
        alignText="left"
    ) 
    
    #PRACTICE SEQUENCE
    postPracOutcome = visual.TextStim(
        win, 
        text='Practice complete! \n\nDetermining outcomes...', 
        pos = (0,0),
        color=[1,1,1],
        height = textHeight,
        wrapWidth = wrap,
        alignText="left"
    )
    
    postTask1 = visual.TextStim(
        win, 
        text='ROUND 1 of the task is complete! \n\nDetermining outcomes...', 
        pos = (0,0),
        color=[1,1,1],
        height = textHeight,
        wrapWidth = wrap,
        alignText="left"
    )
    
    postTask2 = visual.TextStim(
        win, 
        text='ROUND 2 of the task is complete! \n\nDetermining outcomes...', 
        pos = (0,0),
        color=[1,1,1],
        height = textHeight,
        wrapWidth = wrap,
        alignText="left"
    )
    
    postTask3 = visual.TextStim(
        win, 
        text='ROUND 3 of the task is complete! \n\nDetermining outcomes...', 
        pos = (0,0),
        color=[1,1,1],
        height = textHeight,
        wrapWidth = wrap,
        alignText="left"
    )
    
    postTask4 = visual.TextStim(
        win, 
        text='ROUND 4 of the task is complete! \n\nDetermining outcomes...', 
        pos = (0,0),
        color=[1,1,1],
        height = textHeight,
        wrapWidth = wrap,
        alignText="left"
    )
    
    ocSelect = visual.TextStim(
        win,  
        pos = (0,0),
        color=[1,1,1],
        height =textHeight,
        wrapWidth=wrap,
        alignText="left"
    )

    earnings_txt = visual.TextStim(
        win,  
        pos = (0,0),
        color=[1,1,1],
        height =textHeight,
        wrapWidth=wrap,
        alignText="left"
    )
    
    #GET STIMULI READY FOR ENTIRE TASK
    # prep stuff for choice display
    circle = visual.Circle(
        win=win,
        units="pix",
        radius=radius,
        fillColor=[1, 1, 1],
        lineColor=[1, 1, 1],
        edges =128 #make the circle smoother
    )
    
    
    # text for v and n choice buttons:
    vTxt = visual.TextStim(
        win=win,
        text='V - Left',
        color = [1,1,1],
        font='Helvetica',
        pos=[centerL[0],100-radius*1.5],
        height =textHeight
    )
    
    
    nTxt = visual.TextStim(
        win=win,
        text='N - Right',
        color = [1,1,1],
        font='Helvetica',
        pos=[centerR[0],100-radius*1.5],
        height =textHeight
    )
    
    #draw a line that will intersect the gamble circle:
    line = visual.Line( 
        win = win,
        units="pix",
        lineColor = [-1,-1,-1]
    )
    
    #set up text format for $ amounts, text and position will vary each trial:
    gainTxt = visual.TextStim(
        win=win,
        color = [-1,-1,-1],
        font='Helvetica',
        height =moneyTextHeight
    )
    
    earningsTxt = visual.TextStim(
        win=win,
        text='Earnings: $',
        color = [1,1,1],
        font='Helvetica',
        height = textHeight * 1.2,
        #pos = (-0.9, 0.9)
        pos = topL,
        alignText = 'right'
    )

    goalTxt = visual.TextStim(
        win=win,
        text = 'Goal: $',
        color = [1,1,1],
        font = "Helvetica",
        height = textHeight * 1.2
    )
    
    bonusTxt = visual.TextStim(
        win=win,
        text='Bonus: $',
        color = [1,1,1],
        font='Helvetica',
        height = textHeight * 1.2,
        #pos = (0.9, 0.9)
        pos = topR,
        alignText = 'left'
    )
    
    lossTxt = visual.TextStim(
        win=win,
        color = [-1,-1,-1],
        font='Helvetica',
        height =moneyTextHeight
    )
    
    altTxt = visual.TextStim(
        win=win,
        color = [-1,-1,-1],
        font='Helvetica',
        height =moneyTextHeight
    )
    
    orTxt = visual.TextStim(
        win=win,
        text="OR",
        pos=center,
        color = [1,1,1],
        font='Helvetica',
        height =textHeight
    )
    
    #ISI STIMULI
    isiStim = visual.TextStim(
        win = win,
        units = "pix",
        pos = center,
        text='+',
        height = textHeight
    )
    
    itiStim = isiStim
    
    # OUTCOME stimuli
    noRespTxt = visual.TextStim(
        win=win,
        text='You did not respond in time.',
        color = [1,1,1],
        font='Helvetica',
        pos=center,
        height =textHeight,
        wrapWidth = wrap
    )
    
    #black rectangles to cover up half the circle during outcome period, position will vary
    rect4win = visual.Rect( 
        win=win,
        units="pix",
        width=rectWidth,
        height=rectHeight,
        fillColor=[-1, -1, -1],
        lineColor=[-1, -1, -1],
    )
    
    rect4loss = visual.Rect( 
        win=win,
        units="pix",
        width=rectWidth,
        height=rectHeight,
        fillColor=[-1, -1, -1],
        lineColor=[-1, -1, -1],
    )
    
    ocCircle = visual.Circle(
        win=win,
        units="pix",
        radius=radius,
        fillColor=[1, 1, 1],
        lineColor=[1, 1, 1],
        edges =128 #make the circle smoother
    )
    
    # PROGRESS BARS
    # this is the dimension where the progres bar starts
    progBarStart = [scrnsize[1]*-.45,scrnsize[1]*-.375]
    progBarEnd = [progBarStart[0]+5,progBarStart[1]]
    
    progBar = visual.Line(
        win, 
        start=progBarStart, 
        end=progBarEnd, 
        units='pix', 
        lineWidth=textHeight*.35, 
        lineColor='white'
    )
    
    progBarOutline = visual.Rect(
        win, 
        width=((progBarStart[0]*-1)+10)*2, 
        height=textHeight/2, 
        units='pix', 
        pos=[center[0],progBarStart[1]], 
        lineColor = "white", 
        fillColor=None
    )
    
    
    # Text for for progress bar (text will dynamically update below)
    progressTxt = visual.TextStim(
        win,
        color="white",
        pos =[progBarStart[0]+25,-360],
        height = textHeight/2
    ) 
    
    
    # ---- START INSTRUCTIONS + PRACTICE ---- #
    
    mes2.draw()
    win.flip()
    event.waitKeys(keyList = ['q'], timeStamped = False) # waiting for key press or until max time allowed
    
    inst1.draw()
    win.flip()
    event.waitKeys(keyList = ['q'], timeStamped = False) # waiting for key press or until max time allowed
    
    inst2.draw()
    win.flip()
    event.waitKeys(keyList = ['q'], timeStamped = False) # waiting for key press or until max time allowed
    
    pracBorderBox.draw()
    blackBox.draw()
    inst3.draw()
    win.flip()
    core.wait(forcedInstrWaitTime)
    event.waitKeys(keyList = ['v', 'n'], timeStamped = False) # waiting for key press or until max time allowed
    
    #------------------PRACTICE TRIALS-----------------#
    
    # Participants do the practice trials once.
    

    #nPract=3 # number of practice trials
    itiPract = 1, 1.5, 1, 2, 1 
    
    #practice values (same for all participants):
    gainPract = 53.17, 6.45, 28.16, 8.50, 30.54
    lossPract =0, 0, 0, 0, 0
    safePract = 27.89, 5.10, 17.05, 4.12, 17.25

    # DATA SAVE
    practiceData = [] # create data structure with column names
    practiceData.append(
        [
            "riskyGain", 
            "riskyLoss", 
            "safe", 
            "RT", 
            "loc", 
            "response", 
            "choice",
            "outcome",
            "iti",
            "itiExtra",
            "stimDispStart",
            "choiceTimeStart",
            "isiStart",
            "outcomeDispStart",
            "itiStart",
            "trial"
        ]
    )
        
    # round_earnings added above

    # define variable that is used to change the size of the progress bar
    changeInBar = int((progBarStart[0]/nPract)*-1)*2 # double it because it needs to go across the entire screen (not just half)
    
    
    pracStart = core.Clock() # starts clock for practice 


    round_earnings = 0

    for p in range(nPract):
        
        t = p+1 # to make t (trial) = 1 since python starts at 0
    
        
        progBar.end += [changeInBar,00] # update end point of progress bar
        progressTxt.text = text= "Trial %d/%d " % (t,nPract)
        
        pracBorderBox.draw()
        blackBox.draw()
        progressTxt.draw() # draws the message to the window, but only during the loop
        progBarOutline.draw()
        progBar.draw()
    
        #ADD TOP TEXT
        earningsTxt.text = text='Earnings: $%.2f' % round_earnings
        goalTxt.text = text = 'Goal: $%.2f' % goalPract
        bonusTxt.text = text='Bonus: $%.2f' % bonusPract
        
        gainTxt.text = text='$%.2f' % gainPract[p]
        lossTxt.text = text='$%.2f' % lossPract[p]
        altTxt.text = text='$%.2f' % safePract[p]

    # randomly choose location of gamble on screen
        loc = random.choice([1,2]) 
        #loc = 1; gamble on left, alt on right
        #loc = 2; gamble on the right, alt on left
    
        if loc == 1:
            lnstart=lnGamL[0]
            lnend= lnGamL[1]
            gainpos= gainGamL
            losspos = lossGamL
            altpos=altGamL
            rectGainPos = [centerL[0], centerL[1]+(radius*.5)]
            rectLossPos = [centerL[0], centerL[1]-(radius*.5)]
            #ADD TOP TEXT
            earningsTxt.pos = [centerR[0],scrnsize[1]*.4]
            goalTxt.pos = [center[0],scrnsize[1]*.4]
            bonusTxt.pos = [centerL[0],scrnsize[1]*.4]
        elif loc == 2:
            lnstart=lnGamR[0]
            lnend= lnGamR[1]
            gainpos= gainGamR
            losspos = lossGamR
            altpos=altGamR
            rectGainPos = [centerR[0], centerR[1]+(radius*.5)]
            rectLossPos = [centerR[0], centerR[1]-(radius*.5)]
            #ADD TOP TEXT
            earningsTxt.pos = [centerR[0],scrnsize[1]*.4]
            goalTxt.pos = [center[0],scrnsize[1]*.4]
            bonusTxt.pos = [centerL[0],scrnsize[1]*.4]
    
    
    
    #now that we know the location of gamble, where will the text go?:
        gainTxt.pos = gainpos
        lossTxt.pos = losspos
        altTxt.pos = altpos
    
    # set line start and finish based on loc settings
        line.start=[lnstart,100]
        line.end = [lnend,100]
        line.lineWidth= 5
    
    #draw the stuff
        pracBorderBox.draw() # draw the large color box
        blackBox.draw() # draw smaller black box on top of our color rect to create border effect
        progressTxt.draw() # draws the message to the window, but only during the loop
        progBarOutline.draw()
        progBar.draw()
    
        for side in [-1, 1]:
            circle.pos= [centerL[0]*side,100]
            circle.draw() #draw two circles
        #ADD TOP TEXT
        earningsTxt.draw()
        goalTxt.draw()
        bonusTxt.draw()
        line.draw()
        orTxt.draw()
        altTxt.draw()
        
        gainTxt.draw()
        lossTxt.draw()
        
        response = [] # reset response variable
        choiceTimeStart = []
        rtClock=core.Clock() #start the clock and wait for a response
        
        #port.setData(1)
        win.flip() #show the choice options, keep stimuli on the screen
        stimDispStart = pracStart.getTime()
        response = event.waitKeys(maxWait = stimTime, keyList = ['v', 'n'], timeStamped = rtClock) # waiting for key press
        
        if response is None:
            pracBorderBox.draw()
            blackBox.draw()
            progressTxt.draw() 
            progBarOutline.draw()
            progBar.draw()        
        
            # draw stimuli again with v and n displayed
            for side in [-1, 1]:
                circle.pos= [centerL[0]*side,100]
                circle.draw() #draw two circles

            
            #ADD TOP TEXT
            earningsTxt.draw()
            goalTxt.draw()
            bonusTxt.draw()
            line.draw()
            orTxt.draw()
            altTxt.draw()
            
            gainTxt.draw()
            lossTxt.draw()
            vTxt.draw()
            nTxt.draw()

            win.flip() #show the choice options, keep stimuli on the screen
            choiceTimeStart = pracStart.getTime()
            response = event.waitKeys(maxWait = choiceTime, keyList = ['v', 'n'], timeStamped = rtClock) # waiting for key press
            
            # output from response is ['n', 5.136503931000334] whre its the response key and the current time on rtClock

            
        #response = event.waitKeys(maxWait = stimTime + choiceTime, keyList = ['v', 'n'], timeStamped = False) # waiting for key press or until max time allowed
        if response is None:
            RT = 'NaN'
            choice = 'NaN'
            outcome = 'NaN'
            itiExtra = 0
        elif ['v'] or ['n'] in response[0][0]:
            RT=response[0][1]
            itiExtra = (stimTime + choiceTime)-RT # time that gets added on to the end of the trial
            # record what their choice is based on response and location of gamble on screen
            if loc == 1 and response[0][0] == 'v' or loc ==2 and response[0][0] == 'n': #they gambled
                choice = 1
                outcome = random.choice([gainPract[p],lossPract[p]])
            elif loc==1 and response[0][0] == 'n' or loc==2 and response[0][0] =='v': #they took safe
                choice = 0
                outcome = safePract[p]
            round_earnings += outcome

    
    
        if outcome == gainPract[p]:
            rect = rect4win
            rect.pos = rectLossPos
            ocCircle.pos = [gainpos[0],100] #draw the circle on the side where gamble was displayed
            ocTxt = gainTxt
        elif outcome == lossPract[p]:
            rect = rect4loss
            rect.pos= rectGainPos
            ocCircle.pos = [gainpos[0],100] # draw the circle on the side where gamble was displayed
            ocTxt = lossTxt
        elif outcome == safePract[p]:
            ocCircle.pos = [altpos[0],100] #draw circle on the side that safe option was displayed
            ocTxt = altTxt
    
    
    
        #DO THE ISI
        pracBorderBox.draw()
        blackBox.draw()
        earningsTxt.draw()
        goalTxt.draw()
        bonusTxt.draw()
        progressTxt.draw() # draws the message to the window, but only during the loop
        progBarOutline.draw()
        progBar.draw()
            
        
        isiStim.draw()
        #port.setData(0)
        win.flip() # show it
        isiStart = pracStart.getTime()
        core.wait(isi)
    
        #DO THE OUTCOME
        pracBorderBox.draw()
        blackBox.draw()
        earningsTxt.text = text='Earnings: $%.2f' % round_earnings
        
        if outcome == 'NaN':
            ocTxt = noRespTxt
        else:
            ocCircle.draw()
            ocTxt.draw()
            if outcome == gainPract[p] or outcome == lossPract[p]:
                rect.draw()
            #round_earnings += outcome
    
        
        progressTxt.draw() # draws the message to the window, but only during the loop
        progBarOutline.draw()
        #ADD TOP TEXT
        earningsTxt.draw()
        goalTxt.draw()
        bonusTxt.draw()
        progBar.draw()   
        ocTxt.draw()
        
        #port.setData(1)
        win.flip() # show it
        outcomeDispStart = pracStart.getTime()
        core.wait(outcomeTime)
    
        #ITI    
        itiStart = pracStart.getTime()
        #port.setData(0)
        while pracStart.getTime() < t*(stimTime + choiceTime + isi + outcomeTime) + sum(itiPract[0:t]):
            
            pracBorderBox.draw()
            blackBox.draw()
            #ADD TOP TEXT
            earningsTxt.draw()
            goalTxt.draw()
            bonusTxt.draw()
            progressTxt.draw() # draws the message to the window, but only during the loop
            progBarOutline.draw()
            progBar.draw()
                
            itiStim.draw()
            win.flip()
            
        #DATA SAVE
        # save data on a trial by trial basis
        practiceData.append(
            [
                gainPract[p], 
                lossPract[p], 
                safePract[p], 
                RT, 
                loc, 
                response, 
                choice,
                outcome,
                itiPract[p],
                itiExtra,
                stimDispStart,
                choiceTimeStart,
                isiStart,
                outcomeDispStart,
                itiStart,
                t
            ]
        )
    
    #PRACTICE SEQUENCE
    postPracOutcome.draw()
    win.flip()
    core.wait(2)
        

    if round_earnings >= goalPract:
        ocSelect.text= text='PRACTICE ROUND\n\nYou earned $%.2f over the span of the trials.\n\nThis met the goal of $%.2f. \n\nYou will gain this round‘s bonus of $%.2f.\n\nPress ‘space’ to continue.' % (round_earnings, goalPract, bonusPract)
    else:
        ocSelect.text= text='PRACTICE ROUND\n\nYou earned $%.2f over the span of the trials.\n\nThis did not meet the goal of $%.2f. \n\nYou will not gain this round‘s bonus of $%.2f. \n\nPress ‘space’ to continue.' % (round_earnings, goalPract, bonusPract)
    pracBorderBox.draw()
    blackBox.draw()
    ocSelect.draw() #"You will receive ..."
    win.flip()
    core.wait(2)
    event.waitKeys(keyList = ['space'], timeStamped = False) # waiting for key press     
    
    postPrac.draw()
    win.flip()
    print("Practice trials complete!")
    event.waitKeys(keyList = ['q'], timeStamped = False) # waiting for q or space key press or until max time allowed



#----------Start the task---------#
#try:

#DATA SAVE
    data = [] # create data structure with column names
    data.append(
        [
            "subID",
            "riskyGain", 
            "riskyLoss", 
            "safe", 
            "RT", 
            "round_earnings",
            "curr_goal",
            "curr_bonus",
            "loc", 
            "response", 
            "choice",
            "outcome",
            "iti",
            "itiExtra",
            "cond",
            "stimDispStart",
            "choiceTimeStart",
            "isiStart",
            "outcomeDispStart",
            "itiStart",
            "trial",
            "roundRDM",
            "roundColor",
            "ischecktrial"
        ]
    )
    
    
    # define the increment for increasing progress bar based on number of trials 
    changeInBar = int((progBarStart[0]/nT)*-1)*2 # double it because it needs to go across the entire screen (not just half)
    
    for r in range(RDMrounds):
        #reset the progress bar end point at the start of each round
        progBar.end = progBarEnd 
            
        # which progress bar and outline will we show?
        curr_color = colors[colorOrder[r]] # get the color for the current round
        borderBox.fillColor = curr_color # set the border color for the current round

        # randomize trials 
        staticDF = staticDF.sample(frac = 1).reset_index(drop = True) # use pandas to take all the rows and randomize them
            
        # store some of the choice set features in new variables
        riskyGain = staticDF['riskyoption1']
        riskyLoss = staticDF['riskyoption2']
        safe = staticDF['safeoption']
        ischecktrial = staticDF['ischecktrial']

        itiStatic = [] # intertrial interval
        itiStatic = [0.75, 1.25] * 25 # jittered between 0.75 and 1.25 seconds for all 50 trials (BUT THERE'S ITIEXTRA!)
        shuffle(itiStatic)

    
        # show our round separation theatric stuff (include forced viewing period when appropriate)
        if r == 0: 
            explainGPRRounds1.draw()
            win.flip()
            core.wait(forcedInstrWaitTime)
            
            explainGPRRounds1.draw()
            win.flip()
            event.waitKeys(keyList = ['space'], timeStamped=False)

            readyForRound1.draw()
            win.flip()
            core.wait(forcedInstrWaitTime)
            event.waitKeys(keyList = ['space'], timeStamped=False)
            
        elif r > 0:
            postRoundCheck.draw()
            win.flip()
            core.wait(forcedInstrWaitTime)

            postRoundCheck.draw()
            win.flip()
            event.waitKeys(keyList = ['space'], timeStamped=False)
        

        # round_val = cond[r]; # store strategy value (0/1/2/3)  
        curr_bonus = condition_levels[cond[r]][0]
        curr_goal = condition_levels[cond[r]][1]

        #Attempting to change the HIGH/LOW variable with each condition as needed
        #level = "HIGH", "LOW"
        if curr_bonus == HIGH_BONUS:
            bonus_level_txt = "HIGH"
        else:
            bonus_level_txt = "LOW"


        keepLoopGoing = True
        
        if r == 1:
            readyForRound2.draw()
            win.flip()
            core.wait(forcedInstrWaitTime)
            event.waitKeys(keyList = ['space'], timeStamped=False)
        elif r == 2:
            readyForRound3.draw()
            win.flip()
            core.wait(forcedInstrWaitTime)
            event.waitKeys(keyList = ['space'], timeStamped=False)
        elif r == 3:
            readyForRound4.draw()
            win.flip()
            core.wait(forcedInstrWaitTime)
            event.waitKeys(keyList = ['space'], timeStamped=False)

        # HIGH/LOW variable change
        controlInstGPR.text = "In this round, your goal is $%.2f. \n\nYour bonus in this round is %s ($%.2f). \n\nTake a moment if you need before beginning the task. \n\nPress 'V' or 'N' when you are ready to begin." % (curr_goal, bonus_level_txt, curr_bonus)

        borderBox.draw() # draw the large color box
        blackBox.draw() # draw smaller black box on top of our color rect to create border effect
                
        controlInstGPR.draw()                           
        win.flip()
        core.wait(2)
        event.waitKeys(keyList = ['v', 'n'], timeStamped = False)

        
        rdmStart = core.Clock() # starts clock for rdm task 
        round_earnings = 0
            
        for t in range(nT):
            

            s = t+1 # new counter that starts at 1 since python starts at 0

                        
            progBar.end += [changeInBar,00]
            progressTxt.text = text= "Trial %d/%d " % (s,nT)
            
            
            gainTxt.text = text='$%.2f' % riskyGain[t]
            lossTxt.text = text='$%.2f' % riskyLoss[t]
            altTxt.text = text='$%.2f' % safe[t]
            earningsTxt.text = text='Earnings: $%.2f' % round_earnings
            goalTxt.text = text = 'Goal: $%.2f' % curr_goal
            bonusTxt.text = text='Bonus: $%.2f' % curr_bonus
    
        
        # randomly choose location of gamble on screen
            loc = random.choice([1,2]) 
        #loc = 1; gamble on left, alt on right
        #loc =2; gamble on the right, alt on left
            
            if loc == 1:
                lnstart=lnGamL[0]
                lnend= lnGamL[1]
                gainpos= gainGamL
                losspos = lossGamL
                altpos=altGamL
                rectGainPos = [centerL[0], centerL[1]+(radius*.5)]
                rectLossPos = [centerL[0], centerL[1]-(radius*.5)]
            elif loc == 2:
                lnstart=lnGamR[0]
                lnend= lnGamR[1]
                gainpos= gainGamR
                losspos = lossGamR
                altpos=altGamR
                rectGainPos = [centerR[0], centerR[1]+(radius*.5)]
                rectLossPos = [centerR[0], centerR[1]-(radius*.5)]
        
        #now that we know the location of gamble, where will the text go?:
            gainTxt.pos = gainpos
            earningsTxt.pos = [centerR[0],scrnsize[1]*.4]
            goalTxt.pos = [center[0],scrnsize[1]*.4]
            bonusTxt.pos = [centerL[0],scrnsize[1]*.4]
            lossTxt.pos = losspos
            altTxt.pos = altpos
        
        # set line start and finish based on loc settings
            line.start=[lnstart,100]
            line.end = [lnend,100]
            line.lineWidth= 5
        
        #draw the stuff (YAS)
            borderBox.draw() # draw the large color box
            blackBox.draw() # draw smaller black box on top of our color rect to create border effect
            progressTxt.draw() # draws the message to the window, but only during the loop
            progBarOutline.draw()
            progBar.lineColor = curr_color # set the color of the progress bar
            progBar.draw()
            
            
            for side in [-1, 1]:
                circle.pos= [centerL[0]*side,100]
                circle.draw() #draw two circles
            line.draw()
            orTxt.draw()
            altTxt.draw()
            gainTxt.draw()
            earningsTxt.draw()
            goalTxt.draw()
            bonusTxt.draw()
            lossTxt.draw()
            
    
            response = [] # reset response variable
            choiceTimeStart = []
            rtClock=core.Clock() #start the clock and wait for a response
        
    
            stimDispStart = rdmStart.getTime()
            #port.setData(1)
            win.flip() #show the choice options, keep stimuli on the screen
            response = event.waitKeys(maxWait = stimTime, keyList = ['v', 'n'], timeStamped = rtClock) # waiting for key press
            
            if response is None:
                borderBox.draw() # draw the large color box
                blackBox.draw() # draw smaller black box on top of our color rect to create border effect
                progressTxt.draw() 
                progBarOutline.draw()
                progBar.draw()        
            
                # draw stimuli again with v and n displayed
                for side in [-1, 1]:
                    circle.pos= [centerL[0]*side,100]
                    circle.draw() #draw two circles
            
                line.draw()
                orTxt.draw()
                altTxt.draw()
                gainTxt.draw()
                earningsTxt.draw()
                goalTxt.draw()
                bonusTxt.draw()
                lossTxt.draw()
                vTxt.draw()
                nTxt.draw()
    
                win.flip() #show the choice options, keep stimuli on the screen
                choiceTimeStart = rdmStart.getTime()
                response = event.waitKeys(maxWait = choiceTime, keyList = ['v', 'n'], timeStamped = rtClock) # waiting for key press
                
                # output from response is ['n', 5.136503931000334] whre its the response key and the current time on rtClock
    
                
            #response = event.waitKeys(maxWait = stimTime + choiceTime, keyList = ['v', 'n'], timeStamped = False) # waiting for key press or until max time allowed
            if response is None:
                RT = 'NaN'
                choice = 'NaN'
                outcome = 'NaN'
                itiExtra = 0
            elif ['v'] or ['n'] in response[0][0]:
                RT=response[0][1]
                itiExtra = (stimTime + choiceTime)-RT # time that gets added on to the end of the trial
                # record what their choice is based on response and location of gamble on screen
                if loc == 1 and response[0][0] == 'v' or loc ==2 and response[0][0] == 'n': #they gambled
                    choice = 1
                    outcome = random.choice([riskyGain[t],riskyLoss[t]])
                elif loc==1 and response[0][0] == 'n' or loc==2 and response[0][0] =='v': #they took safe
                    choice = 0
                    outcome = safe[t]
                round_earnings += outcome


            if choice == 1:
                if outcome == riskyGain[t]:
                    rect = rect4win
                    rect.pos = rectLossPos
                    ocCircle.pos = [gainpos[0],100] #draw the circle on the side where gamble was displayed
                    ocTxt = gainTxt
                elif outcome == riskyLoss[t]:
                    rect = rect4loss
                    rect.pos= rectGainPos
                    ocCircle.pos = [gainpos[0],100] # draw the circle on the side where gamble was displayed
                    ocTxt = lossTxt
            elif choice == 0:
                ocCircle.pos = [altpos[0],100] #draw circle on the side that safe option was displayed
                ocTxt = altTxt
        
        
            #DO THE ISI
            borderBox.draw() # draw the large color box
            blackBox.draw() # draw smaller black box on top of our color rect to create border effect
            progressTxt.draw() # draws the message to the window, but only during the loop
            progBarOutline.draw()
            progBar.draw()
            earningsTxt.draw()
            goalTxt.draw()
            bonusTxt.draw()

            isiStim.draw()
            #port.setData(0)
            win.flip() # show it
            isiStart = rdmStart.getTime()
            core.wait(isi)
        
            #DO THE OUTCOME
            earningsTxt.text = text='Earnings: $%.2f' % round_earnings
            borderBox.draw() # draw the large color box
            blackBox.draw() # draw smaller black box on top of our color rect to create border effect
            progressTxt.draw() # draws the message to the window, but only during the loop
            progBarOutline.draw()
            progBar.draw()
            
            if outcome == 'NaN':
                ocTxt = noRespTxt
            else:
                ocCircle.draw()
                ocTxt.draw()
                if choice == 1: # if it was a risky choice & outcome
                    rect.draw()
                    
            
            ocTxt.draw()
            earningsTxt.draw()
            goalTxt.draw()
            bonusTxt.draw()
            #port.setData(1)
            win.flip() # show it
            outcomeDispStart = rdmStart.getTime()
            core.wait(outcomeTime)
        
            #ITI 
            itiStart = rdmStart.getTime()
            #port.setData(0)
            while rdmStart.getTime() < s*(stimTime + choiceTime + isi + outcomeTime) + sum(itiStatic[0:s]):
                borderBox.draw() # draw the large color box
                blackBox.draw() # draw smaller black box on top of our color rect to create border effect
                progressTxt.draw() # draws the message to the window, but only during the loop
                progBarOutline.draw()
                earningsTxt.draw()
                goalTxt.draw()
                bonusTxt.draw()
                progBar.draw()
                itiStim.draw()
                win.flip()
                #core.wait(iti[t])
            


    #DATA SAVE    
        # save data on a trial by trial basis
            data.append(
                [
                    subID,
                    riskyGain[t], 
                    riskyLoss[t], 
                    safe[t], 
                    RT,
                    round_earnings,
                    curr_goal,
                    curr_bonus, 
                    loc, 
                    response, 
                    choice,
                    outcome,
                    itiStatic[t],
                    itiExtra,
                    cond[r],
                    stimDispStart,
                    choiceTimeStart,
                    isiStart,
                    outcomeDispStart,
                    itiStart,
                    t,
                    r+1,
                    colorOrder[r],
                    ischecktrial[t]
                ]
            )

        
        datatopickoutcomes = pd.DataFrame(data[1:len(data)], columns = data[0]) # convert to dataframe
        datatopickoutcomes = datatopickoutcomes.loc[datatopickoutcomes['roundRDM'] == (r+1)]; # just want the one round
        allOutcomes = datatopickoutcomes['outcome'] # save just the outcomes
        
        # select an outcome to pay participant
        realOutcomes = datatopickoutcomes[allOutcomes != 'NaN'] 
    
        
        trialSelected = np.random.choice(realOutcomes['trial']) # randomly select a trial
        ocSelected = realOutcomes['outcome'][realOutcomes['trial']==trialSelected] # pull out outcome based on randomly selected trial
        ocSelected = ocSelected.iat[0] # this removes the extra information like float, name, etc.
        
        
        borderBox.draw() # draw the large color box
        blackBox.draw() # draw smaller black box on top of our color rect to create border effect
        
        if r ==0:
            postTask1.draw() #"randomly selecting outcome..."
        elif r==1:
            postTask2.draw()
        elif r==2:
            postTask3.draw()
        elif r==3:
            postTask4.draw()
        win.flip()
        core.wait(2)
        
        round_bonus = 0


        if round_earnings >= curr_goal:
            ocSelect.text= text="ROUND %i\n\nYou earned $%.2f over the span of the trials.\n\nThis met the goal of $%.2f. \n\nYou will gain this round's bonus of $%.2f.\n\nPress ‘space’ to continue." % (r+1, round_earnings, curr_goal, curr_bonus)
            round_bonus += curr_bonus
        else:
            ocSelect.text= text="ROUND %i\n\nYou earned $%.2f over the span of the trials.\n\nThis did not meet the goal of $%.2f. \n\nYou will not gain this round's bonus of $%.2f. \n\nPress ‘space’ to continue." % (r+1, round_earnings,curr_goal, curr_bonus)
        
        all_round_bonuses[r] = round_bonus
        all_round_earnings[r] = round_earnings

        borderBox.draw() # draw the large color box
        blackBox.draw() # draw smaller black box on top of our color rect to create border effect
        ocSelect.draw() #"You will receive ..."
        win.flip()
        core.wait(2)
        event.waitKeys(keyList = ['space'], timeStamped = False) # waiting for key press 
        
        if r == 3:
            callExperimenter.draw()
            win.flip()
            event.waitKeys(keyList = ['q'], timeStamped = False) # waiting for key press     
            win.close()

        
    dataDF = pd.DataFrame(data)
    
    #Addition for total outcome and earnings, make sure to scale by 0.009 or 0.9%
    total_earnings = sum(all_round_earnings)
    total_bonuses = sum(all_round_bonuses)
    total_compensation = total_earnings + total_bonuses

    scale_factor = 0.009

    final_dollar_compensation = total_compensation * scale_factor

    earnings_txt.text = ""
    for r in range(RDMrounds):
        earnings_txt.text = earnings_txt.text + "Round %i: Earnings: $%.2f, Bonus: $%.2f\n" % (r+1, all_round_earnings[r], all_round_bonuses[r])
    earnings_txt.text = earnings_txt.text + "\nTOTAL EARNED: $%.2f\n\nAfter scaling by %.1f%%, real dollars earned = $%.2f" % (total_compensation, scale_factor*100, final_dollar_compensation)

    compensation = [] # create data structure with column names
    compensation.append(
        [
            "roundearnings",
            "roundbonus", 
            "totalcompensation", 
            "finaldollarcompensation"
        ]
    )
    for r in range(RDMrounds):
        compensation.append(
            [
                all_round_earnings[r],
                all_round_bonuses[r],
                [],
                []
            ]
        )
    compensation.append(
        [
            [],
            [],
            total_compensation,
            final_dollar_compensation
        ]
    )
    
#Add the overall_bonus to the round_earnings --> The current code only counts what happens in the last round of the task. Also make sure not to include the round_earnings from the practice rounds.

    earnings_txt.draw()
    win.flip()
    event.waitKeys(keyList = ['q'], timeStamped = False) # waiting for key press 

        
    #finally: # this should save the data even if something in "try" fails
    win.close()
    
    datetime = time.strftime("%Y%m%d-%H%M%S"); # save date and time
    
    #DATA SAVE
    if 'data' in locals(): 
        if not isinstance(data, pd.DataFrame):
            data = pd.DataFrame(data)
            # data.columns = ["subID","riskyGain", "riskyLoss","safe", "RT", "loc", "response", "choice","outcome","itiStatic","itiExtra","evLevel","evInd","runSize","strategy","stimDispStart","choiceTimeStart","isiStart","outcomeDispStart","itiStart","trial","roundRDM","roundColor"]
            data.columns = ["subID","riskyGain", 
            "riskyLoss", "safe", "RT", "round_earnings","curr_goal","curr_bonus","loc", "response", "choice", "outcome", "iti", "itiExtra", "cond", "stimDispStart", "choiceTimeStart", "isiStart", "outcomeDispStart", "itiStart", "trial", "roundRDM", "roundColor","ischecktrial"]
            data = data.iloc[1: , :] # drop the first row which are the variable names
        filenameRDM = dataDirectoryPath + "gprRDM_" + "sub" + subID + "_" + datetime + ".csv"; # make filename
        data.to_csv(filenameRDM)

    #DATA SAVE        
    if 'practiceData' in locals(): 
        if not isinstance(practiceData, pd.DataFrame):
            practiceData = pd.DataFrame(practiceData) #convert data into pandas dataframe
            practiceData.columns=["riskyGain", "riskyLoss", "safe", "RT", "loc", "response", "choice","outcome","iti","itiExtra","stimDispStart","choiceTimeStart","isiStart","outcomeDispStart","itiStart","trial"] # add column names
            practiceData = practiceData.iloc[1: , :] # drop the first row which are the variable practiceData.iloc[1: , :] # drop the first row which are the variable names
        filenamePrac = dataDirectoryPath + "gprRDMpractice_" + "sub" + subID + "_" + datetime + ".csv"; # make filename
        practiceData.to_csv(filenamePrac)

    if 'compensation' in locals():
        if not isinstance(compensation, pd.DataFrame):
            compensation = pd.DataFrame(compensation)
            compensation.columns = ["roundearnings",
                    "roundbonus", 
                    "totalcompensation", 
                    "finaldollarcompensation"]
            compensation = compensation.iloc[1: , :] # drop the first row which are the variable names
        filenameGPRcomp = dataDirectoryPath + "gprBonusCompensation_" + "sub" + subID + "_" + datetime + ".csv"; # make filename
        compensation.to_csv(filenameGPRcomp)



