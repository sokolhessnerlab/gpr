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


import pandas


def rcsRDM(subID, cond1, cond2, cond3, cond4, cond1color, cond2color, cond3color, cond4color, isReal, dirName, dataDirName):
    
    
    #subID='001'
    #cond1 = 0
    #cond2 = 1
    #cond1color = 0
    #cond2color = 1
    #isReal (1 = yes, 0 = testing)
    
    try:   
    
        # Import modules we need
        import random, time, os
        import pandas as pd
        from psychopy import visual, core, event, monitors
        import numpy as np
        import sys
        
        # change directory
        #os.chdir('/Users/hayley/Documents/Github/rcs/rdmTask') # hb mac
        #os.chdir('/Users/shlab/Documents/Github/rcs/task/rdmTask') # mahimahi
        #os.chdir('/Users/Display/Desktop/Github/rcs/rdmTask') # tofu
        os.chdir(dirName + 'rdmTask')
        
        
        #dataDirectoryPath = '/Users/shlab/Documents/Github/rcs/task/data/'
        #dataDirectoryPath = dirName + 'data/'
        dataDirectoryPath = dataDirName + "rdmData/"
    
        
        # Import the choice set function
        #from rcsRDMChoiceSet import *
        sys.path.append(os.path.dirname(__file__))
        sys.path.append(os.path.join(os.path.dirname(__file__), 'rdmTask'))
        import rcsRDMChoiceSet
        
        # Define rounds of risky decision-making task
        RDMrounds=4; 
        
        # Store conditions in one structure 
        cond = [cond1, cond2, cond3, cond4] #(0= control, 1 = strategy, 2=something, 3=something else)
        colorOrder = [cond1color, cond2color, cond3color, cond4color] #(green = 0, purple = 1, blue = 2, orange = 3)
        colors = [[0,.6,0], [.5,0,.5], [0,.7,.9], [.9,.6,0]] # green, purple, blue, orange
                  
        curr_color = colors[colorOrder[0]]
        # Set up the experimental parameters that are consistent across task rounds:
        
        # Screen dimensions and drawing stuff
        #scrnsize= [800,800] #how large the screen will be
        scrnsize=[1280,1024] # CORRECT DIMENSIONS FOR REAL TASK
        #scrnsize = [1024,819.2] # 80% of correct size for mac laptop
        center = [0,100]
        centerR = [scrnsize[0]/4,100]
        centerL = [scrnsize[0]/-4,100]
        topR = [scrnsize[0]/4, scrnsize[1]/2]
        topL = [scrnsize[0]/-4, scrnsize[1]/2]
        radius = scrnsize[0]/5.5
        rectHeight = radius +2 #rectangle used to cover up half the circle when outcome is gain or loss
        rectWidth = radius*2+2
        #textHeight = radius/2.1
        textHeight = 40
        moneyTextHeight= textHeight*2
        wrap = scrnsize[0]*.9 # text wrapping
        
        # earned bonus through all tasks 
        earned_bonus = 0
        
        # BONUS values are represented as a dollar amount
        LOW_BONUS = 2
        HIGH_BONUS = 10
        
        # GOAL is represented as a percentile amount of the amount to hit, the dollar amount is calculatred from CSV data from that percentile
        LOW_GOAL = 10
        HIGH_GOAL = 60
        
        df = pandas.read_csv(dirName + "rdmTask/" + 'gpr_percentiles.csv', dtype={"percentile":"int"}) 
        LOW_GOAL_AMOUNT = df.iloc[LOW_GOAL-1]['earnings'] 
        HIGH_GOAL_AMOUNT = df.iloc[HIGH_GOAL-1]['earnings']
        
        condition_levels = [(LOW_BONUS, LOW_GOAL_AMOUNT), (LOW_BONUS, HIGH_GOAL_AMOUNT), (HIGH_BONUS, LOW_GOAL_AMOUNT), (HIGH_BONUS, HIGH_GOAL_AMOUNT)]
        
        if isReal == 1:
            nT = 50
            nPract = 5
        else:    
            nT = 2 #for testing purposes
            nPract = 2
    
        
        
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
        # ITIs are 1, 1.5, or 2s
        
        # set up monitor in lab on mahimahi
        # mon = monitors.Monitor("DELL 1908FP")
        # mon.setSizePix([1280,1024])
        # mon.save()
        
        
        # Set up the window
        win = visual.Window(
            size=scrnsize,
            units="pix",
            fullscr= True, #For FULLSCREEN, type True, for WINDOW type False
            color=[-1, -1, -1], #black screen
            screen=1 # on second screen
        )
        
        
        # set up stimuli to create the green and purple borders
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

        #mes1 = visual.TextStim(
           # win, 
           # text='Setting up...', 
           # pos = (0,0),
           # color=[1,1,1], 
           # height=40
        #)
        
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
            text='Next up are 5 practice trials. \n\nDo you have any questions for the experimenter? \n\nPlease ask the experimenter now.', 
            pos = (0,0),
            color=[1,1,1],
            height = textHeight,
            wrapWidth = wrap,
            alignText="left"
        )
        
        #instGPR2 = visual.TextStim(
           # win,
           # text = "Next, you will complete 5 practice trials. These trials DO NOT count, \n\nand the goal and bonus are for EXAMPLE ONLY. \n\nIf you have any questions for the experimenter \n\nask them now.",
           # pos = (0,0),
           # color = [1,1,1],
           # height = textHeight,
           # wrapWidth = wrap,
           # alignText = "left"
        #)

        #Change to instGPR_
        inst3 = visual.TextStim(
            win, 
            text="Press 'V' or 'N' when you are ready to begin the practice.", 
            pos = (0,0),
            color=[1,1,1],
            height = textHeight,
            wrapWidth = wrap,
            alignText="left"
        )
        
        postPrac = visual.TextStim(
            win, 
            text="Practice complete! \n\nDo you have any questions for the experimenter? \n\nPlease ask the experimenter now. \n\nWhen you are ready, press 'space' to continue.", 
            pos = (0,0),
            color=[1,1,1],
            height = textHeight,
            wrapWidth = wrap,
            alignText="left"
        )
        
        #postPracGPR = visual.TextStim(
           # win,
           # text = "Practice complete! \n\nDo you have any questions for the experimenter? \n\nAsk them now.",
           # pos = (0,0),
           # color = [1,1,1],
           # height = textHeight,
           # wrapWidth = wrap,
           # alightText = "left"
        #)

        # SEPARATION THEATRICS FOR SEPARATING ROUNDS

        #explainRounds1 = visual.TextStim(
           # win, 
           # text = "You are about to do two rounds of the task. \n\nThese rounds are completely independent. \n\nEach round will be marked with a different color (purple or green).\n\nTreat each round of the task as independent.\n\n\nPress 'space' to continue.",
           # pos = (0,0),
           # color=[1,1,1],
           # height = textHeight,
           # wrapWidth = wrap,
           # alignText="left"
        #)
        
        explainGPRRounds1 = visual.TextStim(
            win,
            text = "Today you will be completing four (4) rounds of the task. \n\nThese rounds are completely independent. \n\nEach round will be marked with a different color - purple, green, blue, or yellow - Not necessarily in that order. \n\nEach round will also have different goals and bonuses associated with them. These goals and bonuses will be explained prior to each round. \n\n\nPress 'space' to continue.",
            pos = (0,0),
            color = [1,1,1],
            height = textHeight,
            wrapWidth = wrap,
            alignText = "left"
        )

        # Don't think we need explainRounds2 or explainRounds3 in GPR
        #explainRounds2 = visual.TextStim(
           # win, 
           # text = "Prior to each round, you will read an additional set of instructions.\n\nAfteward, the experimenter will ask for a short, verbal summary of the instructions.\n\nThe experimenter will leave the room prior to each round of the task. \n\nPress 'enter' to continue.",
           # pos = (0,0),
           # color=[1,1,1],
           # height = textHeight,
           # wrapWidth = wrap,
           # alignText="left"
        #)
        
        #explainRounds3 = visual.TextStim(
           # win, 
           # text = "After each round of the gambling task, you will be asked two short questions.\n\nThe computer will tell you when you should press the white button to call the experimenter back into the room.\n\n\nPress 'enter' to continue.",
           # pos = (0,0),
           # color=[1,1,1],
           # height = textHeight,
           # wrapWidth = wrap,
           # alignText="left"
        #)
        
        readyForRound1 = visual.TextStim(
            win,
            text='Are you ready for ROUND 1 of the task?\n\n\n\nPress ‘space’ to continue.',
            pos = (0,0),
            color=[1,1,1],
            height=textHeight,
            wrapWidth=wrap,
            alignText="left"
        )

        #readyForRound1GPR = visual.TextStim(
           # win,
           # text = "You'll now begin the real rounds of the task. \n\nRemember, if you reach the goal, you will win the bonus for the round. \n\nEach round is independent of one another, meaning your performance in each round will not impact the results of any of the following rounds. \n\nPress 'space' to continue.",
           # pos = (0,0);
           # color = [1,1,1],
           # height = textHeight,
           # wrapWidth = wrap,
           # alignText = "left"
        #)
        
        round2Prep = visual.TextStim(
            win,
            text="You have completed this round, and will start the next, new round momentarily. \n\nMoving ahead to the next round, do your best to let the outcomes of the previous round go. \n\nFocus instead on the new goal and bonus. Rounds are independent from one another, making each round a new start. \n\nThe outcomes of any given round have no effect on subsequent rounds. \n\nBefore advancing, take a moment to get ready if you need, \n\nand press 'space' when you're ready to continue.",
            pos = (0,0),
            color=[1,1,1],
            height=textHeight,
            wrapWidth=wrap,
            alignText="left"
        )               
        
        #This should be set up to say this for rounds 3 and 4 as well for GPR.
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

        #Don't think we really need this for GPR. 
        #startingRound1 = visual.TextStim(
           # win,
           # text='Setting up ROUND 1...',
           # pos = (0,0),
           # color=[1,1,1],
           # height=textHeight,
           # wrapWidth=wrap,
           # alignText="left"
        #)
        
        
        #startingRound2 = visual.TextStim(
           # win,
           # text='Setting up ROUND 2...',
           # pos = (0,0),
           # color=[1,1,1],
           # height=textHeight,
           # wrapWidth=wrap,
           # alignText="left"
        #)
        
        #   PREPARING FOR THE FIRST ROUND INSTRUCTIONS
        #prepForConditionRound1 = visual.TextStim(
           # win,
           # text='Before we begin ROUND 1 of the gambling task, you will be asked to read some additional task instructions.\n\nPlease pay close attention to the instructions as you read them.\n\n\n\nPress ‘space’ to continue.',
           # pos = (0,0),
           # color=[1,1,1],
           # height=textHeight,
           # wrapWidth=wrap,
           # alignText="left"
        #)
        #This should be called before the slide when participants see the goal and the bonus GPR.
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
        
        
        # PREPARING FOR THE SECOND ROUND OF INSTRUCTIONS
        # if participant is switching conditions from round 1:
        prepForConditionRound2_pg1Switching = visual.TextStim(
            win,
            text='Before we begin ROUND 2 of the gambling task, you will be asked to read additional task instructions that are different from round 1. \n\nThe mechanics of the task will be the exact same but the instructions will ask you to think differently than you did in round 1. \n\nPlease pay close attention to the instructions as you read them.\n\nTry your best to forget the instructions from round 1 and follow these new instructions. \n\n\n\nPress ‘space’ to continue.',
            pos = (0,0),
            color=[1,1,1],
            height=textHeight,
            wrapWidth=wrap,
            alignText="left"
        )
        
        prepForConditionRound2_pg1Repeating= visual.TextStim(
            win,
            text='Before we begin ROUND 2 of the gambling task, you will be asked to read a brief reminder of the instructions that were given in round 1.\n\n\n\nPress ‘space’ to continue.',
            pos = (0,0),
            color=[1,1,1],
            height=textHeight,
            wrapWidth=wrap,
            alignText="left"
        )
        
        prepForConditionRound2_pg2forAllSubs = visual.TextStim(
            win,
            text='Please let the experimenter know when you are done reading the instructions.\n\n\n\nPress ‘space’ to continue.',
            pos = (0,0),
            color=[1,1,1],
            height=textHeight,
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
        
        #controlInst2 = visual.TextStim(
           # win,
           # text='Knowing how the task works, don’t try to control your thoughts any more than you would normally, and take as much of a natural approach to your decisions as you can, whatever that might mean for you. \n\nMake your choices in a way that makes sense to you, given any goals, rules of thumb, or factors you think or feel are important. \n\n\nPress ‘enter’ to continue.',
           # pos = (0,0),
           # color=[1,1,1],
           # height=textHeight,
           # wrapWidth=wrap,
           # alignText="left"
        #)
        
        #controlInst3 = visual.TextStim(
           # win,
           # text='For this round, focus on the task itself, and the events, options, and actions that you would naturally consider, and how you feel about them. \n\nIf you select the gamble, you have an equal chance of receiving either amount and if you select the safe option, that will be the outcome for that trial.\n\nYou will complete many trials in this round.\n\n\nPress ‘enter’ to continue.',
           # pos = (0,0),
           # color=[1,1,1],
           # height=textHeight,
           # wrapWidth=wrap,
           # alignText="left"
        #)
        
        #controlInst4 = visual.TextStim(
           # win,
           # text='On each trial, let your thoughts, feelings, impulses, and goals guide your decision-making as naturally as possible, without trying to change, eliminate, or emphasize them beyond how you might otherwise naturally. \n\nRemember that you will be paid the outcome of one randomly selected trial, and simply try to make the best choices you can. \n\nFor this round, approach the task and evaluate your choice options as you would naturally, without trying to control or change your approach. \n\n\nPress ‘enter’ to continue.',
           # pos = (0,0),
           # color=[1,1,1],
           # height=textHeight,
           # wrapWidth=wrap,
           # alignText="left"
        #)
        
        
        #controlReminder1  = visual.TextStim(
           # win,
           # text='As a reminder, in this round of the task, please make your choices however you normally would.\n\nOn each trial, let your thoughts, feelings, impulses, and goals guide your decision-making as naturally as possible, without trying to change, eliminate, or emphasize them beyond how you might otherwise naturally. \n\n\nPress ‘enter’ to continue.',
           # pos = (0,0),
           # color=[1,1,1],
           # height=textHeight,
           # wrapWidth=wrap,
           # alignText="left"
        #)
        
        #controlReminder2 = visual.TextStim(
           # win,
           # text='Simply try to make the best choices you can.\n\nFor this round, approach the task and evaluate your choice options as you would naturally, without trying to control or change your approach.\n\n\nPress ‘enter’ to continue.',
           # pos = (0,0),
           # color=[1,1,1],
           # height=textHeight,
           # wrapWidth=wrap,
           # alignText="left"
        #)
        
        
        # STRATEGY INSTRUCTIONS (FIRST TIME AROUND)
        
        #stratInst1 = visual.TextStim(
           # win,
           # text='In this round of the task, please make your choices in isolation from any context, considering each choice solely on its own merits. \n\nIn our previous studies involving this gambling task, we have found that participants’ choices to accept the gamble were influenced not only by the options on the current trial but also depended on what happened earlier in the task.\n\n\nPress ‘enter’ to continue.',
           # pos = (0,0),
           # color=[1,1,1],
           # height=textHeight,
           # wrapWidth=wrap,
           # alignText="left"
        #)
        
        #stratInst2 = visual.TextStim(
           # win,
           # text='Each trial in this task is unrelated to previous trials. \n\nThe values and outcomes of previous trials do not influence the outcome of the current trial. \n\nAllowing previous values and outcomes to influence your current choice may lead to a lower payoff, and thus not maximize the money you receive.\n\n\nPress ‘enter’ to continue.',
           # pos = (0,0),
           # color=[1,1,1],
           # height=textHeight,
           # wrapWidth=wrap,
           # alignText="left"
        #)
        
        #stratInst3 = visual.TextStim(
           # win,
           # text='For each decision in this round, focus on the monetary values on the screen, the probability of receiving each of those options, and how you feel about them. \n\nForget about the previous values, choices, and outcomes and simply focus on the current trial. \n\nIf you select the gamble, you have an equal chance of receiving either amount and if you select the safe option, that will be the outcome for that trial. \n\nThis is true regardless of what has happened earlier in the task. \n\n\nPress ‘enter’ to continue.',
           # pos = (0,0),
           # color=[1,1,1],
           # height=textHeight,
           # wrapWidth=wrap,
           # alignText="left"
        #)
        
        #stratInst4 = visual.TextStim(
           # win,
           # text='Remember that you will be paid the outcome of one randomly selected trial.\n\nOn each trial, think about how you would feel if the outcome on this trial was randomly selected as your cash payment.\n\nFor this round, approach the task and evaluate your choice options with a focus on only that choice, in isolation from any context.\n\n\nPress ‘enter’ to continue.',
           # pos = (0,0),
           # color=[1,1,1],
           # height=textHeight,
           # wrapWidth=wrap,
           # alignText="left"
        #)
        
        #strategyReminder1  = visual.TextStim(
           # win,
           # text='As a reminder, in this round of the task, please make your choices in isolation from any context, considering each choice solely on its own merits.\n\nOn each trial, focus on the monetary values on the screen, the probability of receiving each of those options, and how you feel about them.\n\n\nPress ‘enter’ to continue.',
           # pos = (0,0),
           # color=[1,1,1],
           # height=textHeight,
           # wrapWidth=wrap,
           # alignText="left"
        #)
        
        #strategyReminder2 = visual.TextStim(
           # win,
           # text='Forget about the previous values, choices, and outcomes and simply focus on the current trial.\n\nThink about how you would feel if the outcome on this trial was randomly selected as your cash payment.\n\nFor this round, approach the task and evaluate your choice options with a focus on only that choice, in isolation from any context.\n\n\nPress ‘enter’ to continue.',
           # pos = (0,0),
           # color=[1,1,1],
           # height=textHeight,
           # wrapWidth=wrap,
           # alignText="left"
        #)
        
        # screen count for instructions
        instructCount = visual.TextStim(
            win,
            pos =[scrnsize[1]*.95,-360],
            color=[1,1,1],
            height=textHeight/2,
            wrapWidth=wrap,
            alignText="left"
        ) 
        
        
        #summarizeInst = visual.TextStim(
           # win,
           # text='Please let the experimenter know that you are done reading the instructions. \n\nIf you wish to read the instructions again, press "R".',
           # pos = (0,0),
           # color=[1,1,1],
           # height=textHeight,
           # wrapWidth=wrap,
           # alignText="left"
        #)
        
        # I don't think I'm going to be leaving the room for GPR in any of the rounds
        #startTaskRound1 = visual.TextStim(
           # win, 
           # text='The experimenter will now leave the room.\n\nOnce the experimenter leaves the room, you may begin ROUND 1 of the gambling task. \n\nPress "V" or "N" to begin the task.', 
           # pos = (0,0),
           # color=[1,1,1],
           # height = textHeight,
           # wrapWidth =wrap,
           # alignText="left"
        #)
        
        
        #startTaskRound2 = visual.TextStim(
           # win, 
           # text='The experimenter will now leave the room.\n\nOnce the experimenter leaves the room, you may begin ROUND 2 of the gambling task. \n\nPress "V" or "N" to begin the task.', 
           # pos = (0,0),
           # color=[1,1,1],
           # height = textHeight,
           # wrapWidth = wrap,
           # alignText="left"
        #)
        
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
            pos = topL
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
            pos = topR
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
        
        #ISI STIMULI (iti will use same stimuli):
        # isiStim = visual.Circle(
        #     win=win,
        #     units="pix",
        #     pos=center,
        #     radius=1.5,
        #     fillColor=[1, 1, 1],
        #     lineColor=[1, 1, 1],
        #     edges =128 #make the circle smoother
        # )
        
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
        #mes1.draw()
        #win.flip()
        #core.wait(1)
        
        mes2.draw()
        win.flip()
        event.waitKeys(keyList = ['q'], timeStamped = False) # waiting for key press or until max time allowed
        
        inst1.draw()
        win.flip()
        event.waitKeys(keyList = ['q'], timeStamped = False) # waiting for key press or until max time allowed
        
        inst2.draw()
        win.flip()
        event.waitKeys(keyList = ['q'], timeStamped = False) # waiting for key press or until max time allowed
        
        inst3.draw()
        win.flip()
        event.waitKeys(keyList = ['v', 'n'], timeStamped = False) # waiting for key press or until max time allowed
        
        
        #------------------PRACTICE TRIALS-----------------#
        
        # Participants do the practice trials once.
        
        #nPract=3 # number of practice trials
        itiPract = 1, 1.5, 1, 2, 1 
        
        #practice values (same for all participants):
        gainPract = 53.17,6.45, 28.16, 8.50,30.54
        lossPract =0,0,0,0,0
        safePract = 27.89,5.10,17.05,4.12,17.25
        
        
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
            
        
        # define variable that is used to change the size of the progress bar
        changeInBar = int((progBarStart[0]/nPract)*-1)*2 # double it because it needs to go across the entire screen (not just half)
        
        
        pracStart = core.Clock() # starts clock for practice 
        #pracStart.reset() # resets the clock
            
        for p in range(nPract):
            
            t = p+1 # to make t (trial) = 1 since python starts at 0
        
            
            progBar.end += [changeInBar,00] # update end point of progress bar
            progressTxt.text = text= "Trial %d/%d " % (t,nPract)
            
            progressTxt.draw() # draws the message to the window, but only during the loop
            progBarOutline.draw()
            progBar.draw()
        
            gainTxt.text = text='$%.2f' % gainPract[p]
            lossTxt.text = text='$%d' % lossPract[p]
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
            lossTxt.pos = losspos
            altTxt.pos = altpos
        
        # set line start and finish based on loc settings
            line.start=[lnstart,100]
            line.end = [lnend,100]
            line.lineWidth= 5
        
        #draw the stuff
        
        
            for side in [-1, 1]:
                circle.pos= [centerL[0]*side,100]
                circle.draw() #draw two circles
            line.draw()
            orTxt.draw()
            altTxt.draw()
            gainTxt.draw()
            lossTxt.draw()
            stimDispStart = pracStart.getTime()
            
    
            response = [] # reset response variable
            choiceTimeStart = []
            rtClock=core.Clock() #start the clock and wait for a response
        
    
            win.flip() #show the choice options, keep stimuli on the screen
            response = event.waitKeys(maxWait = stimTime, keyList = ['v', 'n'], timeStamped = rtClock) # waiting for key press
            
            if response is None:
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
            progressTxt.draw() # draws the message to the window, but only during the loop
            progBarOutline.draw()
            progBar.draw()   
            
            isiStim.draw()
            win.flip() # show it
            isiStart = pracStart.getTime()
            core.wait(isi)
        
            #DO THE OUTCOME
            if outcome == 'NaN':
                ocTxt = noRespTxt
            else:
                ocCircle.draw()
                ocTxt.draw()
                if outcome == gainPract[p] or outcome == lossPract[p]:
                    rect.draw()
        
            pracBorderBox.draw()
            blackBox.draw()
            progressTxt.draw() # draws the message to the window, but only during the loop
            progBarOutline.draw()
            progBar.draw()   
            ocTxt.draw()
            win.flip() # show it
            outcomeDispStart = pracStart.getTime()
            core.wait(outcomeTime)
        
            #ITI    
            itiStart = pracStart.getTime()
            while pracStart.getTime() < t*(stimTime + choiceTime + isi + outcomeTime) + sum(itiPract[0:t]):
                
                progressTxt.draw() # draws the message to the window, but only during the loop
                progBarOutline.draw()
                progBar.draw()   
                itiStim.draw()
                win.flip()
                
            
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
        
        overall_outcome = outcome

    #if --> How is practice defined here in terms of r
        if overall_outcome >= 60:
            ocSelect.text= text='PRACTICE ROUND\n\nYou earned $%d over the span of the trials.\n\nThis met the goal of $60 \n\nYou will gain this rounds bonus of $5\n\nPress ‘space’ to continue.' % (overall_outcome)
        else:
            ocSelect.text= text='PRACTICE ROUND\n\nYou earned $%d over the span of the trials.\n\nThis did not meet the goal of $60 \n\nYou will not gain this rounds bonus of $5 \n\nPress ‘space’ to continue.' % (overall_outcome)
        # pracBorderBox.draw() # draw the large color box
        # blackBox.draw() # draw smaller black box on top of our color rect to create border effect
        ocSelect.draw() #"You will receive ..."
        win.flip()
        event.waitKeys(keyList = ['space'], timeStamped = False) # waiting for key press     
        
        postPrac.draw()
        win.flip()
        print("Practice trials complete!")
        event.waitKeys(keyList = ['space', 'q'], timeStamped = False) # waiting for q or space key press or until max time allowed
    
    
    #practiceData = pd.DataFrame(practiceData) #convert data into pandas dataframe
    
    
    # save practice file
    #datetime = time.strftime("%Y%m%d-%H%M%S"); # save date and time
    #filename = "rcsRDMpractice_" + "sub" + subID + "_" + datetime + ".csv"; # make filename
    #practiceData.to_csv(filename)
    
    
    #----------Start the task---------#
    #try:
    
        data = [] # create data structure with column names
        data.append(
            [
                "subID",
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
                "evLevel",
                "evInd",
                "runSize",
                "strategy",
                "stimDispStart",
                "choiceTimeStart",
                "isiStart",
                "outcomeDispStart",
                "itiStart",
                "trial",
                "roundRDM",
                "roundColor"
            ]
        )
        
        postQdata=[]
        postQdata.append(
            [
                "subID",
                "difficulty",
                "howOften"
            ]
        )
    
        trialOutcome = []
        trialOutcome.append(
            [
                "subID",
                "trial",
                "outcome"
            
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

            # generate the choiceset on each round and save the choice set
            rcsCS = rcsRDMChoiceSet.rcsRDMChoiceSet()
            
            # save the choice set for each round of the task
            rcsCSdf = pd.DataFrame(rcsCS)
    
            # save file
            datetime = time.strftime("%Y%m%d-%H%M%S"); # save date and time
            filenameRDMchoiceset = dataDirectoryPath + "rcsRDM_choiceSet_round" + str(r) + "_sub" + subID + "_" + datetime + ".csv"; # make filename
            rcsCSdf.to_csv(filenameRDMchoiceset)
                
           
            # store some of the choice set features in new variables
            riskyGain = rcsCS['riskyGain']
            riskyLoss = rcsCS['riskyLoss']
            safe = rcsCS['alternative']
            evLevel = rcsCS['evLevel']
            evInd = rcsCS['evInd']
            runSize = rcsCS['runSize']
        
        
            #ITIs change as a function of choiceset
            iti = rcsCS['iti']
        
    
            # show our round separation theatric stuff (include forced viewing period when appropriate)
            if r == 0: 
                explainGPRRounds1.draw()
                win.flip()
                core.wait(forcedInstrWaitTime)
                
                explainGPRRounds1.draw()
                win.flip()
                event.waitKeys(keyList = ['space'], timeStamped=False)
                
                #explainRounds2.draw()
                #win.flip()
                #core.wait(forcedInstrWaitTime)
                
                #explainRounds2.draw()
                #win.flip()
                #event.waitKeys(keyList = ['return'], timeStamped=False)
                
                #explainRounds3.draw()
                #win.flip()
                #core.wait(forcedInstrWaitTime)
                
                #explainRounds3.draw()
                #win.flip()
                #event.waitKeys(keyList = ['return'], timeStamped=False)
                
                #borderBox.draw() # draw the large color box
                #blackBox.draw() # draw smaller black box on top of our color rect to create border effect

                readyForRound1.draw()
                win.flip()
                core.wait(forcedInstrWaitTime)
                event.waitKeys(keyList = ['space'], timeStamped=False)
                
               # startingRound1.draw()
               # win.flip()
               # core.wait(1)
            
            #Make this more clear for GPR --> This is true for all rounds after 0 (Round 1)
            elif r > 0:
                round2Prep.draw()
                win.flip()
                core.wait(forcedInstrWaitTime)

                round2Prep.draw()
                win.flip()
                event.waitKeys(keyList = ['space'], timeStamped=False)
                
                #This needs to be changed so that when preparing for the next rounds the people see rounds 2,3,4 and not just round 2
                #readyForRoundOther.draw()
                #win.flip()
                #event.waitKeys(keyList = ['space'], timeStamped=False)
                
                #startingRound2.draw()
                #win.flip()
                #core.wait(1)

                
    
            """
            Depending on round and whether participant is switching, we will show 
            slightly different instructions. 
            
            If its round 1, participants will read the full
            instructions for the assigned condition. 
            
            If its round 2 and the participant is switching conditions, 
            they will read a screen that tells them they will be reading new 
            instructions, then they will read the new instructions in their entirety.
            
            If its round 2 and the participant is repeating conditions, participants
            will be told they will read a reminder and then they will read the reminder 
            instructions.
            
            All participants will be asked to summarize the instructions no matter the round
            or condition or switching/repeating.
            """
            
            # set up border color
            #borderBox.draw() # draw the large color box
            #blackBox.draw() # draw smaller black box on top of our color rect to create border effect
            
    
            # the first screen in the series of instructions gives the participant a heads up 
            # that instructions are coming up.
            
            strategy = cond[r]; # store strategy value (0/1/2/3)  
            curr_bonus = condition_levels[strategy][0]
            curr_goal = condition_levels[strategy][1]

            # if r >= 0:
            #controlInstGPR.draw()
            #win.flip()
            #event.waitKeys(keyList = ['v','n'], timeStamped=False)

        #if r == 0:
            # prepForConditionRound1GPR.draw() #"Before we begin ROUND 1..."
            # this is the same for all participants, just one screen
        #elif r==1 and cond[r] == cond[r-1]: # if we are in the second round and participant is repeating conditions
            # prepForConditionRound2_pg1Repeating.draw() #"Before we begin ROUND 2..." first page of instructions in round 1
        #elif r==1 and cond[r] != cond[r-1]: # if we are in the second round and participant is switching conditions
            # prepForConditionRound2_pg1Switching.draw() 
            
        #win.flip()
        #event.waitKeys(keyList = ['space'], timeStamped = False) # waiting for key press
        
        #if r==1: # round 2 has a second page of prep instructions
            # set up border color
            #borderBox.draw() # draw the large color box
            #blackBox.draw() # draw smaller black box on top of our color rect to create border effect
            
            # draw and show page 2, wait for response
            #prepForConditionRound2_pg2forAllSubs.draw()
            #win.flip()
            #event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press

    # Determine the condition specific instructions    
            # strategy = cond[r]; # store strategy value (0/1/2/3)  
            # curr_bonus = condition_levels[strategy][0]
            # curr_goal = condition_levels[strategy][1] 
            
            #Offer participants the option to re-read the instructions where they can pres 'R' after page 4
            keepLoopGoing = True
            #while keepLoopGoing:  
            
                #if r == 0 or r==1 and strategy!=cond[r-1]: # round 1 or switiching in round 2, we show the full control or strategy instructions
        
                    #if strategy == 0: # if the condition is control
                        #instructPG1 = controlInstGPR
                        #instructPG2 = controlInst2
                        #instructPG3 = controlInst3
                        #instructPG4 = controlInst4
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

                    # CHECK TO SEE IF THIS WORKS
            if r==0:
                controlInstGPR.text = text="In this round, your goal is $%d. \n\nYour bonus in this round is HIGH/LOW ($%d). \n\nTake a moment if you need before beginning the task. \n\nPress 'V' or 'N' when you are ready to begin." % (curr_goal, curr_bonus)
            elif r==1:
                controlInstGPR.text = text="In this round, your goal is $%d. \n\nYour bonus in this round is HIGH/LOW ($%d). \n\nTake a moment if you need before beginning the task. \n\nPress 'V' or 'N' when you are ready to begin." % (curr_goal, curr_bonus)
            elif r==2:
                controlInstGPR.text = text="In this round, your goal is $%d. \n\nYour bonus in this round is HIGH/LOW ($%d). \n\nTake a moment if you need before beginning the task. \n\nPress 'V' or 'N' when you are ready to begin." % (curr_goal, curr_bonus)
            elif r==3:
                controlInstGPR.text = text="In this round, your goal is $%d. \n\nYour bonus in this round is HIGH/LOW ($%d). \n\nTake a moment if you need before beginning the task. \n\nPress 'V' or 'N' when you are ready to begin." % (curr_goal, curr_bonus)

            instructPG1 = controlInstGPR        
                    #elif strategy == 1: # if the condition is strategy
                        #instructPG1 = stratInst1
                        #instructPG2 = stratInst2
                        #instructPG3 = stratInst3
                        #instructPG4 = stratInst4
        
        
                    #show page 1 + forced viewing
            borderBox.draw() # draw the large color box
            blackBox.draw() # draw smaller black box on top of our color rect to create border effect
                    
                    #instructPG1.draw()
                    #instructCount.text=text="screen 1/4"
                    #instructCount.draw()
        
                    #win.flip()
                    #core.wait(forcedInstrWaitTime)

                    # show page 1 + repsonse collection
            #borderBox.draw() # draw the large color box
            #blackBox.draw() # draw smaller black box on top of our color rect to create border effect
                    
            instructPG1.draw()
                    #instructCount.text=text="screen 1/4"
            #instructCount.draw()                    
            win.flip()
                    #event.waitKeys(keyList = ['space'], timeStamped = False) # waiting for key press 
            event.waitKeys(keyList = ['v', 'n'], timeStamped = False)

                    #show page 2 + forced viewing
                    #borderBox.draw() # draw the large color box
                    #blackBox.draw() # draw smaller black box on top of our color rect to create border effect
                    
                    #instructPG2.draw()
                    #instructCount.text=text="screen 2/4"
                    #instructCount.draw()
        
                    #win.flip()
                    #core.wait(forcedInstrWaitTime)
                    
                    
                    # show page 2 + repsonse collection
                    #borderBox.draw() # draw the large color box
                    #blackBox.draw() # draw smaller black box on top of our color rect to create border effect
                    
                    #instructPG2.draw()
                    #instructCount.text=text="screen 2/4"
                    #instructCount.draw()
        
                    #win.flip()
                    #event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press 
                    
                    
                    #show page 3 + forced viewing
                    #borderBox.draw() # draw the large color box
                    #blackBox.draw() # draw smaller black box on top of our color rect to create border effect
                    
                    #instructPG3.draw()
                    #instructCount.text=text="screen 3/4"
                    #instructCount.draw()
        
                    #win.flip()
                    #core.wait(forcedInstrWaitTime)
                    
                    # show page 3 + repsonse collection
                    #borderBox.draw() # draw the large color box
                    #blackBox.draw() # draw smaller black box on top of our color rect to create border effect
                    
                    #instructPG3.draw()
                    #instructCount.text=text="screen 3/4"
                    #instructCount.draw()
        
                    #win.flip()
                    #event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press 
                    
                    #show page 4 + forced viewing
                    #borderBox.draw() # draw the large color box
                    #blackBox.draw() # draw smaller black box on top of our color rect to create border effect
                    
                    #instructPG4.draw()
                    #instructCount.text=text="screen 4/4"
                    #instructCount.draw()
        
                    #win.flip()
                    #core.wait(forcedInstrWaitTime)
                    
                    #show page 4 + response collection
                    #borderBox.draw() # draw the large color box
                    #blackBox.draw() # draw smaller black box on top of our color rect to create border effect
                    
                    #instructPG4.draw()
                    #instructCount.text=text="screen 4/4"
                    #instructCount.draw()
        
                    #win.flip()
                    #event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press 
                
                #elif r==1 and strategy==cond[r-1]: # if round 2 and repeting condition (two instead of 4 pages)
                # if  strategy ==0: # if control condition
                    # instructPG1 = controlReminder1
                    # instructPG2 = controlReminder2
                        
                # elif strategy ==1: # if strategy condition
                    # instructPG1 = strategyReminder1
                    # instructPG2 = strategyReminder2
        
                    #show page 1 + forced viewing
                # borderBox.draw() # draw the large color box
                # blackBox.draw() # draw smaller black box on top of our color rect to create border effect
                    
                # instructPG1.draw()
                    #instructCount.text=text="screen 1/2"
                # instructCount.draw()
                    
                # win.flip()
                # core.wait(forcedInstrWaitTime)
                    
                    
                    #show page 1 + response collection
                # borderBox.draw() # draw the large color box
                # blackBox.draw() # draw smaller black box on top of our color rect to create border effect
                    
                # instructPG1.draw()
                    #instructCount.text=text="screen 1/2"
                # instructCount.draw()
                    
                # win.flip()
                # event.waitKeys(keyList = ['space'], timeStamped = False) # waiting for key press 
                    
                    #show page 2 + forced viewing
                # borderBox.draw() # draw the large color box
                # blackBox.draw() # draw smaller black box on top of our color rect to create border effect
                    
                    #instructPG2.draw()
                    #instructCount.text=text="screen 2/2"
                    #instructCount.draw()
        
                    #win.flip()
                    #core.wait(forcedInstrWaitTime)

                    #show page 2 + response collection
                # borderBox.draw() # draw the large color box
                # blackBox.draw() # draw smaller black box on top of our color rect to create border effect
                    
                    #instructPG2.draw()
                    #instructCount.text=text="screen 2/2"
                    #instructCount.draw()
        
                    #win.flip()
                    #event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press 
        
        
        
                # Now the rest is mostly the same for all participants/conditions/switching show the summarize prompt
            #borderBox.draw() # draw the large color box
            #blackBox.draw() # draw smaller black box on top of our color rect to create border effect
                
                #summarizeInst.draw()
                #win.flip()
                
                
            #keys = event.waitKeys(keyList = ['space','r'], timeStamped = False) # waiting for key press
                #print(keys)
                
                #print(keys[0] == 'return')
                
            #if keys[0] == 'space':
                #keepLoopGoing=False # end loop, start task
            #else:
                #keepLoopGoing=True
            
            #print(f'Round {r} color: {curr_color}')
            #borderBox.draw() # draw the large color box
            #blackBox.draw() # draw smaller black box on top of our color rect to create border effect
            
            # depending on round of task, show slightly different start screen
            #if r==0:
            # startTaskRound1.draw()
            #elif r==1:
            # startTaskRound2.draw()
                
            #win.flip()
            #event.waitKeys(keyList = ['v', 'n'], timeStamped = False) # waiting for key press or until max time allowed
            # experimenter leaves the room, participant starts round 1 of the study
            
            rdmStart = core.Clock() # starts clock for rdm task 
            overall_outcome = 0
                
            for t in range(nT):
                
    
                s = t+1 # new counter that starts at 1 since python starts at 0
    
                            
                progBar.end += [changeInBar,00]
                progressTxt.text = text= "Trial %d/%d " % (s,nT)
                
                
                gainTxt.text = text='$%.2f' % riskyGain[t]
                lossTxt.text = text='$%d' % riskyLoss[t]
                altTxt.text = text='$%.2f' % safe[t]
                earningsTxt.text = text='Earnings: $%.2f' % overall_outcome
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
                stimDispStart = rdmStart.getTime()
                
        
                response = [] # reset response variable
                choiceTimeStart = []
                rtClock=core.Clock() #start the clock and wait for a response
            
        
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
                    overall_outcome += outcome
                earningsTxt.text = text='Earnings: $%.2f' % overall_outcome

    
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
                elif outcome == safe[t]:
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
                win.flip() # show it
                isiStart = rdmStart.getTime()
                core.wait(isi)
            
                #DO THE OUTCOME
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
                    if outcome == riskyGain[t] or outcome == riskyLoss[t]:
                        rect.draw()
                     
                
                ocTxt.draw()
                earningsTxt.draw()
                goalTxt.draw()
                bonusTxt.draw()
                win.flip() # show it
                outcomeDispStart = rdmStart.getTime()
                core.wait(outcomeTime)
            
                #ITI 
                itiStart = rdmStart.getTime()
                while rdmStart.getTime() < s*(stimTime + choiceTime + isi + outcomeTime) + sum(iti[0:s]):
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
                
    
            
            # save data on a trial by trial basis
                data.append(
                    [
                        subID,
                        riskyGain[t], 
                        riskyLoss[t], 
                        safe[t], 
                        RT, 
                        loc, 
                        response, 
                        choice,
                        outcome,
                        iti[t],
                        itiExtra,
                        evLevel[t],
                        evInd[t],
                        runSize[t],
                        cond[r],
                        stimDispStart,
                        choiceTimeStart,
                        isiStart,
                        outcomeDispStart,
                        itiStart,
                        s,
                        r+1,
                        colorOrder[r]
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
            
            #data.append([ocChosen])
            trialOutcome.append(
                [
                    subID,
                    trialSelected,
                    ocSelected
                ]
            )
            
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
            
            if r==0:
                if overall_outcome >= curr_goal:
                    ocSelect.text= text='ROUND 1\n\nYou earned $%d over the span of the trials.\n\nThis met the goal of $%d \n\nYou will gain this rounds bonus of $%d\n\nPress ‘space’ to continue.' % (overall_outcome, curr_goal, curr_bonus)
                else:
                    ocSelect.text= text='ROUND 1\n\nYou earned $%d over the span of the trials.\n\nThis did not meet the goal of $%d \n\nYou will not gain this rounds bonus of $%d \n\nPress ‘space’ to continue.' % (overall_outcome,curr_goal, curr_bonus)
            elif r==1:
                if overall_outcome >= curr_goal:
                    ocSelect.text= text='ROUND 2\n\nYou earned $%d over the span of the trials.\n\nThis met the goal of $%d \n\nYou will gain this rounds bonus of $%d\n\nPress ‘space’ to continue.' % (overall_outcome, curr_goal, curr_bonus)
                else:
                    ocSelect.text= text='ROUND 2\n\nYou earned $%d over the span of the trials.\n\nThis did not meet the goal of $%d \n\nYou will not gain this rounds bonus of $%d \n\nPress ‘space’ to continue.' % (overall_outcome,curr_goal, curr_bonus)
            elif r==2:
                if overall_outcome >= curr_goal:
                    ocSelect.text= text='ROUND 3\n\nYou earned $%d over the span of the trials.\n\nThis met the goal of $%d \n\nYou will gain this rounds bonus of $%d\n\nPress ‘space’ to continue.' % (overall_outcome, curr_goal, curr_bonus)
                else:
                    ocSelect.text= text='ROUND 3\n\nYou earned $%d over the span of the trials.\n\nThis did not meet the goal of $%d \n\nYou will not gain this rounds bonus of $%d \n\nPress ‘space’ to continue.' % (overall_outcome,curr_goal, curr_bonus)
            elif r==3:
                if overall_outcome >= curr_goal:
                    ocSelect.text= text='ROUND 4\n\nYou earned $%d over the span of the trials.\n\nThis met the goal of $%d \n\nYou will gain this rounds bonus of $%d\n\nPress ‘space’ to continue.' % (overall_outcome, curr_goal, curr_bonus)
                else:
                    ocSelect.text= text='ROUND 4\n\nYou earned $%d over the span of the trials.\n\nThis did not meet the goal of $%d \n\nYou will not gain this rounds bonus of $%d \n\nPress ‘space’ to continue.' % (overall_outcome,curr_goal, curr_bonus)
            borderBox.draw() # draw the large color box
            blackBox.draw() # draw smaller black box on top of our color rect to create border effect
            ocSelect.draw() #"You will receive ..."
            win.flip()
            event.waitKeys(keyList = ['space'], timeStamped = False) # waiting for key press 
            
            # ----------------------
            # COMMENTED OUT POST TASK QUESTIONS FOR NO -- COULD BE REINSTATED OR DELETED ENTIRELY
            # # 2 post-task questions
            # taskRound = r+1 # change the round  to 1 or 2 (versus python's 0 or 1)
            
            
            # # set color of marker and repsonse recorded text
            # sliderColor = [1,1,1] # default color for everything is white
            # curr = colorOrder[r] # current color order for this round
            # if curr == 0:
            #     sliderColor=[0,.6,0] # green
            #     sliderLockPostQ.color=[0,.6,0] 
            # elif curr ==1:
            #     sliderColor=[.5,0,.5] # purple
            #     sliderLockPostQ.color=[.5,0,.5]
            # elif curr == 2:
            #     sliderColor=[0,.7,.9] # blue
            #     sliderLockPostQ.color=[0,.7,.9]
            # elif curr == 3:
            #     sliderColor=[.9,.6,0] # orange
            #     sliderLockPostQ.color=[.9,.6,0]
            
            
            # # Question 1: DIFFICULTY
            # if strategy ==0: # control condition
            #     promptPostQ.text=text="\n\nQuestion 1/2 \n\nFor ROUND %d, you were asked to make your choices as you would naturally, without trying to control or change your approach. \n\n\nUse the slider to rate how DIFFICULT this was. \n\nHover the mouse over the slider to move the marker. Click the mouse when you are done." % taskRound
     
            # elif strategy ==1:
            #     promptPostQ.text=text="\n\nQuestion 1/2 \n\nFor ROUND %d, you were asked to make your choices in isolation from any context, considering each choice solely on its own merits. \n\n\nUse the slider to rate how DIFFICULT this was. \n\nHover the mouse over the slider to move the marker. Click the mouse when you are done." % taskRound
    
        
            # # For some reason, slider.labels is not showing up dynamically, so we reset it here to make labels fit the question
            # print("SliderColor:", sliderColor)
            # slider = visual.Slider(
            #     win, 
            #     size=(scrnsize[0]*.8, 50), 
            #     pos=(0, scrnsize[1]*-.25),
            #     labels = ['Very \neasy', 'Very \ndifficult'],
            #     ticks = [1,100],
            #     granularity=0, 
            #     style=['rating'],
            #     color=sliderColor, 
            #     font='Helvetica',
            #     labelHeight=30,
            # )
    
    
        
            
            # slider_width = slider.size[0]
            # #slider_height = slider.size[1]
            # slider_height = slider.size[1]*3
            # slider_orientation = 0
            # slider_ticks = [0,100]
    
    
    
            # slider_shape = visual.Rect(
            #     win=win, 
            #     name='slider_shape',
            #     width=(slider_width, slider_height)[0], 
            #     height=(slider_width, slider_height)[1],
            #     ori=0, 
            #     pos=slider.pos,
            #     lineWidth=1, 
            #     lineColor='black', 
            #     lineColorSpace='rgb',
            #     fillColor='black', 
            #     fillColorSpace='rgb',
            #     opacity=1, 
            #     depth=-2.0, 
            #     interpolate=True
            # )
    
             
            # slider.markerPos = 50
            # slider.marker.color = sliderColor
            
            # slider_shape.draw()
            # borderBox.fillColor = sliderColor # change the border color to match the slider color
            # borderBox.draw()
            # blackBox.draw()
            # promptPostQ.draw()
            # slider.draw()
    
            # win.flip()
    
            # mouse = event.Mouse(visible = True, win = win) 
            # mouseRec=mouse.getPos()
    
    
    
            # continueRout=True
            # while continueRout:
            #     if slider.markerPos and mouse.isPressedIn(slider_shape):
            #         continueRout = False
            #     elif slider_shape.contains(mouse) and mouse.getPos()[slider_orientation] != mouseRec[slider_orientation]:
            #         mouseRec=mouse.getPos()
            #         slider.markerPos=mouseRec[slider_orientation]/slider_width*(slider_ticks[-1]-slider_ticks[0])+(slider_ticks[0]+slider_ticks[-1])/2
            #         slider_shape.draw()
            #         borderBox.draw()
            #         blackBox.draw()
            #         promptPostQ.draw()
            #         slider.draw()
            #         win.flip()
    
    
                    
            # difficultyRating = slider.markerPos# store rating
            # slider_shape.draw()
            # borderBox.draw() # draw the large color box
            # blackBox.draw() # draw smaller black box on top of our color rect to create border effect
            # sliderLockPostQ.draw() #"rating recorded"
            # promptPostQ.draw()
            # slider.draw()
            # win.flip()
            # core.wait(2)
                            
            
            # # Question 2: HOW OFTEN 
            # if strategy ==0: # control condition
            #     promptPostQ.text=text="\n\nQuestion 2/2 \n\nFor ROUND %d, you were asked to make your choices as you would naturally, without trying to control or change your approach. \n\n\nUse the slider to rate HOW OFTEN you were able to do that. \n\nHover the mouse over the slider to move the marker. Click the mouse when you are done." % taskRound
     
            # elif strategy ==1:
            #     promptPostQ.text=text="\n\nQuestion 2/2 \n\nFor ROUND %d, you were asked to make your choices in isolation from any context, considering each choice solely on its own merits. \n\n\nUse the slider to rate HOW OFTEN you were able to do that.\n\nHover the mouse over the slider to move the marker. Click the mouse when you are done." % taskRound
                
                
                    
            # # For some reason, slider.labels is not showing up dynamically, so we reset it here to make labels fit the question
            # slider = visual.Slider(
            #     win, 
            #     size=(scrnsize[0]*.8, 50), 
            #     pos=(0, scrnsize[1]*-.25),
            #     labels = ['Never', 'Always'],
            #     ticks = [1,100],
            #     granularity=0, 
            #     style=['rating'],
            #     color=sliderColor, 
            #     font='Helvetica',
            #     labelHeight=30,
            # )
    
    
             
            # slider.markerPos = 50
            # slider.marker.color = sliderColor
            
            # slider_shape.draw()
            # borderBox.draw()
            # blackBox.draw()
            # promptPostQ.draw()
            # slider.draw()
    
            # win.flip()
    
            # mouse = event.Mouse(visible = True, win = win) 
            # mouseRec=mouse.getPos()
    
    
    
            # continueRout=True
            # while continueRout:
                
            #     if slider.markerPos and mouse.isPressedIn(slider_shape):
            #         continueRout = False
            #     elif slider_shape.contains(mouse) and mouse.getPos()[slider_orientation] != mouseRec[slider_orientation]:
            #         mouseRec=mouse.getPos()
            #         slider.markerPos=mouseRec[slider_orientation]/slider_width*(slider_ticks[-1]-slider_ticks[0])+(slider_ticks[0]+slider_ticks[-1])/2
            #         slider_shape.draw()
            #         borderBox.draw()
            #         blackBox.draw()
            #         promptPostQ.draw()
            #         slider.draw()
            #         win.flip()
    
    
                    
            # howOftenRating = slider.markerPos # store rating
            # slider_shape.draw()
            # borderBox.draw() # draw the large color box
            # blackBox.draw() # draw smaller black box on top of our color rect to create border effect
            # sliderLockPostQ.draw() #"rating recorded"
            # promptPostQ.draw()
            # slider.draw()
            # win.flip()
            # core.wait(2)
    
    
              
            # postQdata.append(
            #     [
            #         subID,
            #         difficultyRating,
            #         howOftenRating
            #     ]
            # )
            # ----------------------
    
            #press white button for experimenter to come back in the room - it only happens in this spot following round 1
            
            # Make this show up for rounds 2, 3, and 4 also
            if r == 0:
                callExperimenter.draw()
                win.flip()
                event.waitKeys(keyList = ['q'], timeStamped = False) # waiting for key press 
    
            
        #RANDOMLY SELECT OUTCOME FROM BOTH ROUNDS FOR PAYMENT
        trialOutcomeDF = pd.DataFrame(trialOutcome)
        finalOutcomesToSelect = [trialOutcomeDF[2][1], trialOutcomeDF[2][2]]
        outcomeForPay = np.random.choice(finalOutcomesToSelect);
        scaledOC = outcomeForPay/2
        
        #TOTAL EARNINGS PAGE
        ocSelect.text = text = "Across the four rounds of today's study, you earned $Z bonus. \n\nPlease push the white button to call the experimenter now."
        
        #ocSelect.draw()
        #win.flip()
        #event.waitKeys(keyList = ['return'], timeStamped = False) # waiting for key press 
    
    
        #ocSelect.text = text = "Randomly selected outcome: $%.2f. \n\nYou will receive $%.2f as your bonus payment.\n\n\nPress the white button to call the experimenter." % (outcomeForPay, scaledOC)
        #ocSelect.draw()
        #win.flip()
        #event.waitKeys(keyList = ['space'], timeStamped = False) # waiting for key press 
        
        #trialOutcome.append([outcomeForPay]) # save outcome payment.
        #trialOutcome.append([scaledOC])
        
    finally: # this should save the data even if something in "try" fails
        win.close()
        
        
               
        # if data exists, reformat to pandas dataframe if it wasn't above, and save it
        # save practice file
      
        datetime = time.strftime("%Y%m%d-%H%M%S"); # save date and time
        
        if 'data' in locals(): 
            if not isinstance(data, pd.DataFrame):
                data = pd.DataFrame(data)
                data.columns = ["subID","riskyGain", "riskyLoss","safe", "RT", "loc", "response", "choice","outcome","iti","itiExtra","evLevel","evInd","runSize","strategy","stimDispStart","choiceTimeStart","isiStart","outcomeDispStart","itiStart","trial","roundRDM","roundColor"]
                data = data.iloc[1: , :] # drop the first row which are the variable names
            filenameRDM = dataDirectoryPath + "rcsRDM_" + "sub" + subID + "_" + datetime + ".csv"; # make filename
            data.to_csv(filenameRDM)
        
            
        if 'trialOutcome' in locals(): 
            if not isinstance(trialOutcome, pd.DataFrame):
                trialOutcome = pd.DataFrame(trialOutcome) #convert data into pandas dataframe
                trialOutcome.columns=["subID","trial","outcome"] # add column names
                trialOutcome = trialOutcome.iloc[1: , :] # drop the first row which are the variable trialOutcome.iloc[1: , :] # drop the first row which are the variable names
            filenameTrialOutcome = dataDirectoryPath + "rcsTrialOutcome_" + "sub" + subID + "_" + datetime + ".csv"; # make filename
            trialOutcome.to_csv(filenameTrialOutcome)
                
        if 'practiceData' in locals(): 
            if not isinstance(practiceData, pd.DataFrame):
                practiceData = pd.DataFrame(practiceData) #convert data into pandas dataframe
                practiceData.columns=["riskyGain", "riskyLoss", "safe", "RT", "loc", "response", "choice","outcome","iti","itiExtra","stimDispStart","choiceTimeStart","isiStart","outcomeDispStart","itiStart","trial"] # add column names
                practiceData = practiceData.iloc[1: , :] # drop the first row which are the variable practiceData.iloc[1: , :] # drop the first row which are the variable names
            filenamePrac = dataDirectoryPath + "rcsRDMpractice_" + "sub" + subID + "_" + datetime + ".csv"; # make filename
            practiceData.to_csv(filenamePrac)
    
        
        
    
       
    
    
    
    
    
    
    
    
    
