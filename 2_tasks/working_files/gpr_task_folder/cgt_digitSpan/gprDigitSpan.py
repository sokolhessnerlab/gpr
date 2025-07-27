#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.1),
    on July 16, 2025, at 13:30
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
#psychopy.useVersion('2022.2.1')
psychopy.useVersion('2023.2.0')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code
# translated from js

from psychopy import visual, core, event

expName = "Your Experiment Name"  # Replace with your experiment name
expInfo = {"participant": "", "session": ""}  # Replace with your experiment info

resources = [
    {'name': 'digitSpanTrialNumber.xlsx', 'path': 'digitSpanTrialNumber.xlsx'},
    {'name': 'CGT-choice-set.csv', 'path': 'CGT-choice-set.csv'},
    {'name': 'cgtRDMPractice.xlsx', 'path': 'cgtRDMPractice.xlsx'},
    {'name': 'continue.png', 'path': 'continue.png'},
    {'name': 'digitSpanPractice.xlsx', 'path': 'digitSpanPractice.xlsx'},
    # {'name': 'trialTypes_B.xls', 'path': 'http://a.website.org/a.path/trialTypes_B.xls'}
]

# Start the experiment
# Note: You may need to implement the actual start logic based on your requirements


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.1'
expName = 'CGTriskyDMtask'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\jvonm\\Documents\\GitHub\\gpr\\2_tasks\\working_files\\gpr_task_folder\\cgt_digitSpan\\gprDigitSpan.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[2560, 1440], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "settingUp" ---
# Run 'Begin Experiment' code from code
instructionsTextHeight = .05
lettersTextHeight = .1
wrap = 1.5

# --- Initialize components for Routine "SpanGeneralInstructions" ---
# Run 'Begin Experiment' code from setUpTextFormatting_2
instructionsTextHeight = 0.04;
letterTextHeight = 0.1;
wrap = 1.6
GenInsText = visual.TextStim(win=win, name='GenInsText',
    text="In this task you will be asked to memorize a series of numbers and recall them. \n\nYou will do this twice, once recalling the numbers in the order as presented on the screen and once recalling the numbers in the reverse order as presented on the screen. \n\nThere are 14 trials in each direction for a total of 28 trials. \n\nYou will complete 2 practice sets prior to starting each round of this task.\n\nPress 'enter' to continue.",
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=wrap, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
movealong = keyboard.Keyboard()

# --- Initialize components for Routine "SpanReminder1" ---
Reminder1 = visual.TextStim(win=win, name='Reminder1',
    text="Your performance on this task does not affect your compensation. \n\nThis task is supposed to be challenging - you are not expected to nor do you need to remember everything or get everything correct! \n\nPress 'enter' to continue. ",
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=wrap, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
movealong2 = keyboard.Keyboard()

# --- Initialize components for Routine "SpanReminder2" ---
Reminder2 = visual.TextStim(win=win, name='Reminder2',
    text="We are interested in how many digits you can reliably and truthfully recall. \n\nPlease do your best, and do not cheat (e.g. write down or photograph digits). Thank you for completing this task honestly!\n\nPress 'enter' to continue. ",
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=wrap, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
movealong3 = keyboard.Keyboard()

# --- Initialize components for Routine "FSInstructions" ---
FSGenInsText = visual.TextStim(win=win, name='FSGenInsText',
    text='The practice for the forwards section of this task is up next.\n\nYou will complete two practice trials, each with a list of 3 numbers. \n\nType out your answer when "Recall" appears on the screen using the numbers at the top of the keyboard to type out the numbers in the order they were presented on the screen. \n\nDO NOT use spaces or any other symbols (ONLY enter numbers) when you type your answer, otherwise your answer will be counted as incorrect.\n\nFor example, if the numbers displayed on the screen are 5 then 7, the correct response is 57.\n\nIf you make a mistake you can use backspace to correct it.  \n\nFeedback will be provided.\n\nPress \'enter\' to begin the practice.',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=wrap, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
startPractice = keyboard.Keyboard()

# --- Initialize components for Routine "ShowNumbersPractice" ---
fixation_2 = visual.TextStim(win=win, name='fixation_2',
    text='+',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
pres_text_practice = visual.TextStim(win=win, name='pres_text_practice',
    text='',
    font='Arial',
    pos=(0, 0), height=letterTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "RecallPractice" ---
recall_txtPractice = visual.TextStim(win=win, name='recall_txtPractice',
    text='Recall',
    font='Arial',
    pos=(0, 0.25), height=instructionsTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
textboxPractice = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=letterTextHeight,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textboxPractice',
     autoLog=True,
)
cont_buttonPractice = visual.ImageStim(
    win=win,
    name='cont_buttonPractice', 
    image='continue.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -.4), size=(0.3, 0.07),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
mousePractice = event.Mouse(win=win)
x, y = [None, None]
mousePractice.mouseClock = core.Clock()

# --- Initialize components for Routine "FeedbackPractice" ---
feedbac_textPractice = visual.TextStim(win=win, name='feedbac_textPractice',
    text='',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "StartRealFS" ---
praccomplete = visual.TextStim(win=win, name='praccomplete',
    text="Practice complete! \n\nYou are about to begin the forwards section of this task. \n\nYou will start with a list of 3 numbers. If you are able to correctly recall the list of numbers, you will continue to larger lists. \n\nDO NOT use spaces or any other symbols (ONLY enter numbers) when you type your answer, otherwise your answer will be counted as incorrect.\n\nPress 'enter' to start the task.\n",
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=wrap, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
startFSreal = keyboard.Keyboard()

# --- Initialize components for Routine "selectNumbers" ---
# Run 'Begin Experiment' code from selectNumbersFS
numbersToChoose = [1,2,3,4,5,6,7,8,9];
minDigitFS = 3;
maxDigitFS = 16;
#minDigitBS = 2;
#maxDigitBS = 15;
nTrialsFS = 0;
#nTrialsBS = 0;
correct = [];
incorrectCount = 0;


# --- Initialize components for Routine "ShowNumbers" ---
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
presentation_text = visual.TextStim(win=win, name='presentation_text',
    text='',
    font='Arial',
    pos=(0, 0), height=letterTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "Recall" ---
recall_txt = visual.TextStim(win=win, name='recall_txt',
    text='Recall',
    font='Arial',
    pos=(0, 0.25), height=instructionsTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
textbox = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=letterTextHeight,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox',
     autoLog=True,
)
cont_button = visual.ImageStim(
    win=win,
    name='cont_button', 
    image='continue.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -.4), size=(0.3, 0.07),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()

# --- Initialize components for Routine "Feedback" ---
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "FStoBStransition" ---
roundTransition = visual.TextStim(win=win, name='roundTransition',
    text='The first round of the letter task is complete!\n\nPress "enter" to continue to the last round.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
moveToBS = keyboard.Keyboard()

# --- Initialize components for Routine "InstructionsBS" ---
BSGenInsText = visual.TextStim(win=win, name='BSGenInsText',
    text='The practice for the backwards section of this task is up next.\n\nYou will complete two practice trials, each with a list of 2 numbers. \n\nType out your answer when "Recall" appears on the screen using the numbers at the top of the keyboard to type out the numbers in the REVERSE order they were presented on the screen. \n\nFor example, if the numbers presented are 6 then 2, your response should be 26.\n\nPlease DO NOT use spaces or any other symbols (ONLY enter numbers) when you type your answer, otherwise your answer will be counted as incorrect.\n\nIf you make a mistake you can use backspace to correct it.  \n\nFeedback will be provided.\n\nPress \'enter\' to begin the practice.',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=wrap, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
startBSprac = keyboard.Keyboard()

# --- Initialize components for Routine "showNumbersPracticeBS" ---
fixation_3 = visual.TextStim(win=win, name='fixation_3',
    text='+',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
pres_text_practice_2 = visual.TextStim(win=win, name='pres_text_practice_2',
    text='',
    font='Arial',
    pos=(0, 0), height=letterTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "recallPracticeBS" ---
recall_txtPractice_2 = visual.TextStim(win=win, name='recall_txtPractice_2',
    text='Recall',
    font='Arial',
    pos=(0, 0.25), height=instructionsTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
textboxPractice_2 = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=letterTextHeight,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textboxPractice_2',
     autoLog=True,
)
cont_buttonPractice_2 = visual.ImageStim(
    win=win,
    name='cont_buttonPractice_2', 
    image='continue.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -.4), size=(0.3, 0.07),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
mousePractice_2 = event.Mouse(win=win)
x, y = [None, None]
mousePractice_2.mouseClock = core.Clock()

# --- Initialize components for Routine "feedbackPracticeBS" ---
feedbac_textPractice_2 = visual.TextStim(win=win, name='feedbac_textPractice_2',
    text='',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "startRealBS" ---
praccompleteBS = visual.TextStim(win=win, name='praccompleteBS',
    text="Practice complete!\n\nYou are about to begin the backwards section of this task. \n\nYou will start with a list of 2 numbers. If you are able to correctly recall the list of numbers, you will continue to larger lists. \n\nDO NOT use spaces or any other symbols (ONLY enter numbers) when you type your answer, otherwise your answer will be counted as incorrect.\n\nPress 'enter' to start the task.",
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=wrap, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
startBSreal = keyboard.Keyboard()

# --- Initialize components for Routine "selectNumbersBS" ---
# Run 'Begin Experiment' code from selectNumbersBScode
numbersToChoose = [1,2,3,4,5,6,7,8,9];
minDigitBS = 2;
maxDigitBS = 15;
nTrialsBS = 0;
correct = [];
incorrectCount = 0;

# --- Initialize components for Routine "showNumbersBS" ---
fixationBS = visual.TextStim(win=win, name='fixationBS',
    text='+',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
presentation_textBS = visual.TextStim(win=win, name='presentation_textBS',
    text='',
    font='Arial',
    pos=(0, 0), height=letterTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "RecallBS" ---
recall_txtBS = visual.TextStim(win=win, name='recall_txtBS',
    text='Recall',
    font='Arial',
    pos=(0, 0.25), height=instructionsTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
textboxBS = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=letterTextHeight,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textboxBS',
     autoLog=True,
)
cont_buttonBS = visual.ImageStim(
    win=win,
    name='cont_buttonBS', 
    image='continue.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -.4), size=(0.3, 0.07),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
mouseBS = event.Mouse(win=win)
x, y = [None, None]
mouseBS.mouseClock = core.Clock()

# --- Initialize components for Routine "FeedbackBS" ---
feedback_textBS = visual.TextStim(win=win, name='feedback_textBS',
    text='',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "END" ---
ThankYou = visual.TextStim(win=win, name='ThankYou',
    text='Thank you! You have sucessfully completed the second portion of this study.\n\nYou will now be automatically redirected to Qualtrics.',
    font='Arial',
    pos=(0, 0), height=instructionsTextHeight, wrapWidth=wrap, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "settingUp" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
settingUpComponents = []
for thisComponent in settingUpComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "settingUp" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in settingUpComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "settingUp" ---
for thisComponent in settingUpComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "settingUp" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "SpanGeneralInstructions" ---
continueRoutine = True
# update component parameters for each repeat
movealong.keys = []
movealong.rt = []
_movealong_allKeys = []
# keep track of which components have finished
SpanGeneralInstructionsComponents = [GenInsText, movealong]
for thisComponent in SpanGeneralInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "SpanGeneralInstructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *GenInsText* updates
    if GenInsText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        GenInsText.frameNStart = frameN  # exact frame index
        GenInsText.tStart = t  # local t and not account for scr refresh
        GenInsText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(GenInsText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'GenInsText.started')
        GenInsText.setAutoDraw(True)
    
    # *movealong* updates
    waitOnFlip = False
    if movealong.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        movealong.frameNStart = frameN  # exact frame index
        movealong.tStart = t  # local t and not account for scr refresh
        movealong.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(movealong, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'movealong.started')
        movealong.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(movealong.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(movealong.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if movealong.status == STARTED and not waitOnFlip:
        theseKeys = movealong.getKeys(keyList=['return'], waitRelease=False)
        _movealong_allKeys.extend(theseKeys)
        if len(_movealong_allKeys):
            movealong.keys = _movealong_allKeys[-1].name  # just the last key pressed
            movealong.rt = _movealong_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SpanGeneralInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "SpanGeneralInstructions" ---
for thisComponent in SpanGeneralInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if movealong.keys in ['', [], None]:  # No response was made
    movealong.keys = None
thisExp.addData('movealong.keys',movealong.keys)
if movealong.keys != None:  # we had a response
    thisExp.addData('movealong.rt', movealong.rt)
thisExp.nextEntry()
# the Routine "SpanGeneralInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "SpanReminder1" ---
continueRoutine = True
# update component parameters for each repeat
movealong2.keys = []
movealong2.rt = []
_movealong2_allKeys = []
# keep track of which components have finished
SpanReminder1Components = [Reminder1, movealong2]
for thisComponent in SpanReminder1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "SpanReminder1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Reminder1* updates
    if Reminder1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Reminder1.frameNStart = frameN  # exact frame index
        Reminder1.tStart = t  # local t and not account for scr refresh
        Reminder1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Reminder1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Reminder1.started')
        Reminder1.setAutoDraw(True)
    
    # *movealong2* updates
    waitOnFlip = False
    if movealong2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        movealong2.frameNStart = frameN  # exact frame index
        movealong2.tStart = t  # local t and not account for scr refresh
        movealong2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(movealong2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'movealong2.started')
        movealong2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(movealong2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(movealong2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if movealong2.status == STARTED and not waitOnFlip:
        theseKeys = movealong2.getKeys(keyList=['return'], waitRelease=False)
        _movealong2_allKeys.extend(theseKeys)
        if len(_movealong2_allKeys):
            movealong2.keys = _movealong2_allKeys[-1].name  # just the last key pressed
            movealong2.rt = _movealong2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SpanReminder1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "SpanReminder1" ---
for thisComponent in SpanReminder1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if movealong2.keys in ['', [], None]:  # No response was made
    movealong2.keys = None
thisExp.addData('movealong2.keys',movealong2.keys)
if movealong2.keys != None:  # we had a response
    thisExp.addData('movealong2.rt', movealong2.rt)
thisExp.nextEntry()
# the Routine "SpanReminder1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "SpanReminder2" ---
continueRoutine = True
# update component parameters for each repeat
movealong3.keys = []
movealong3.rt = []
_movealong3_allKeys = []
# keep track of which components have finished
SpanReminder2Components = [Reminder2, movealong3]
for thisComponent in SpanReminder2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "SpanReminder2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Reminder2* updates
    if Reminder2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Reminder2.frameNStart = frameN  # exact frame index
        Reminder2.tStart = t  # local t and not account for scr refresh
        Reminder2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Reminder2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Reminder2.started')
        Reminder2.setAutoDraw(True)
    
    # *movealong3* updates
    waitOnFlip = False
    if movealong3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        movealong3.frameNStart = frameN  # exact frame index
        movealong3.tStart = t  # local t and not account for scr refresh
        movealong3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(movealong3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'movealong3.started')
        movealong3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(movealong3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(movealong3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if movealong3.status == STARTED and not waitOnFlip:
        theseKeys = movealong3.getKeys(keyList=['return'], waitRelease=False)
        _movealong3_allKeys.extend(theseKeys)
        if len(_movealong3_allKeys):
            movealong3.keys = _movealong3_allKeys[-1].name  # just the last key pressed
            movealong3.rt = _movealong3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SpanReminder2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "SpanReminder2" ---
for thisComponent in SpanReminder2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if movealong3.keys in ['', [], None]:  # No response was made
    movealong3.keys = None
thisExp.addData('movealong3.keys',movealong3.keys)
if movealong3.keys != None:  # we had a response
    thisExp.addData('movealong3.rt', movealong3.rt)
thisExp.nextEntry()
# the Routine "SpanReminder2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "FSInstructions" ---
continueRoutine = True
# update component parameters for each repeat
startPractice.keys = []
startPractice.rt = []
_startPractice_allKeys = []
# keep track of which components have finished
FSInstructionsComponents = [FSGenInsText, startPractice]
for thisComponent in FSInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "FSInstructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *FSGenInsText* updates
    if FSGenInsText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        FSGenInsText.frameNStart = frameN  # exact frame index
        FSGenInsText.tStart = t  # local t and not account for scr refresh
        FSGenInsText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(FSGenInsText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'FSGenInsText.started')
        FSGenInsText.setAutoDraw(True)
    
    # *startPractice* updates
    waitOnFlip = False
    if startPractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        startPractice.frameNStart = frameN  # exact frame index
        startPractice.tStart = t  # local t and not account for scr refresh
        startPractice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(startPractice, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'startPractice.started')
        startPractice.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(startPractice.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(startPractice.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if startPractice.status == STARTED and not waitOnFlip:
        theseKeys = startPractice.getKeys(keyList=['return'], waitRelease=False)
        _startPractice_allKeys.extend(theseKeys)
        if len(_startPractice_allKeys):
            startPractice.keys = _startPractice_allKeys[-1].name  # just the last key pressed
            startPractice.rt = _startPractice_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FSInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "FSInstructions" ---
for thisComponent in FSInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if startPractice.keys in ['', [], None]:  # No response was made
    startPractice.keys = None
thisExp.addData('startPractice.keys',startPractice.keys)
if startPractice.keys != None:  # we had a response
    thisExp.addData('startPractice.rt', startPractice.rt)
thisExp.nextEntry()
# the Routine "FSInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialFSPractice = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('digitSpanPractice.xlsx'),
    seed=None, name='trialFSPractice')
thisExp.addLoop(trialFSPractice)  # add the loop to the experiment
thisTrialFSPractice = trialFSPractice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialFSPractice.rgb)
if thisTrialFSPractice != None:
    for paramName in thisTrialFSPractice:
        exec('{} = thisTrialFSPractice[paramName]'.format(paramName))

for thisTrialFSPractice in trialFSPractice:
    currentLoop = trialFSPractice
    # abbreviate parameter names if possible (e.g. rgb = thisTrialFSPractice.rgb)
    if thisTrialFSPractice != None:
        for paramName in thisTrialFSPractice:
            exec('{} = thisTrialFSPractice[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    DigitLoopPractice = data.TrialHandler(nReps=3.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='DigitLoopPractice')
    thisExp.addLoop(DigitLoopPractice)  # add the loop to the experiment
    thisDigitLoopPractice = DigitLoopPractice.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisDigitLoopPractice.rgb)
    if thisDigitLoopPractice != None:
        for paramName in thisDigitLoopPractice:
            exec('{} = thisDigitLoopPractice[paramName]'.format(paramName))
    
    for thisDigitLoopPractice in DigitLoopPractice:
        currentLoop = DigitLoopPractice
        # abbreviate parameter names if possible (e.g. rgb = thisDigitLoopPractice.rgb)
        if thisDigitLoopPractice != None:
            for paramName in thisDigitLoopPractice:
                exec('{} = thisDigitLoopPractice[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "ShowNumbersPractice" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_2
        #print(digits) # translated from js
        pres_text_practice.setText(str(digits)[DigitLoopPractice.thisN])
        # keep track of which components have finished
        ShowNumbersPracticeComponents = [fixation_2, pres_text_practice]
        for thisComponent in ShowNumbersPracticeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ShowNumbersPractice" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_2* updates
            if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_2.frameNStart = frameN  # exact frame index
                fixation_2.tStart = t  # local t and not account for scr refresh
                fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_2.started')
                fixation_2.setAutoDraw(True)
            if fixation_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_2.tStop = t  # not accounting for scr refresh
                    fixation_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_2.stopped')
                    fixation_2.setAutoDraw(False)
            
            # *pres_text_practice* updates
            if pres_text_practice.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                pres_text_practice.frameNStart = frameN  # exact frame index
                pres_text_practice.tStart = t  # local t and not account for scr refresh
                pres_text_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pres_text_practice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pres_text_practice.started')
                pres_text_practice.setAutoDraw(True)
            if pres_text_practice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > pres_text_practice.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    pres_text_practice.tStop = t  # not accounting for scr refresh
                    pres_text_practice.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'pres_text_practice.stopped')
                    pres_text_practice.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ShowNumbersPracticeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ShowNumbersPractice" ---
        for thisComponent in ShowNumbersPracticeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine
        routineTimer.addTime(-2.000000)
    # completed 3.0 repeats of 'DigitLoopPractice'
    
    
    # --- Prepare to start Routine "RecallPractice" ---
    continueRoutine = True
    # update component parameters for each repeat
    textboxPractice.reset()
    # setup some python lists for storing info about the mousePractice
    mousePractice.clicked_name = []
    gotValidClick = False  # until a click is received
    # Run 'Begin Routine' code from JScodePractice
    # translated from js
    # this is a temporary fix to allow editable textbox to be used on several trials
    #textboxPractice.refresh()
    # keep track of which components have finished
    RecallPracticeComponents = [recall_txtPractice, textboxPractice, cont_buttonPractice, mousePractice]
    for thisComponent in RecallPracticeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "RecallPractice" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *recall_txtPractice* updates
        if recall_txtPractice.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            recall_txtPractice.frameNStart = frameN  # exact frame index
            recall_txtPractice.tStart = t  # local t and not account for scr refresh
            recall_txtPractice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recall_txtPractice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'recall_txtPractice.started')
            recall_txtPractice.setAutoDraw(True)
        
        # *textboxPractice* updates
        if textboxPractice.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            textboxPractice.frameNStart = frameN  # exact frame index
            textboxPractice.tStart = t  # local t and not account for scr refresh
            textboxPractice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textboxPractice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textboxPractice.started')
            textboxPractice.setAutoDraw(True)
        
        # *cont_buttonPractice* updates
        if cont_buttonPractice.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            cont_buttonPractice.frameNStart = frameN  # exact frame index
            cont_buttonPractice.tStart = t  # local t and not account for scr refresh
            cont_buttonPractice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cont_buttonPractice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cont_buttonPractice.started')
            cont_buttonPractice.setAutoDraw(True)
        # *mousePractice* updates
        if mousePractice.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            mousePractice.frameNStart = frameN  # exact frame index
            mousePractice.tStart = t  # local t and not account for scr refresh
            mousePractice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mousePractice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mousePractice.started', t)
            mousePractice.status = STARTED
            mousePractice.mouseClock.reset()
            prevButtonState = mousePractice.getPressed()  # if button is down already this ISN'T a new click
        if mousePractice.status == STARTED:  # only update if started and not finished!
            buttons = mousePractice.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(cont_buttonPractice)
                        clickableList = cont_buttonPractice
                    except:
                        clickableList = [cont_buttonPractice]
                    for obj in clickableList:
                        if obj.contains(mousePractice):
                            gotValidClick = True
                            mousePractice.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RecallPracticeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "RecallPractice" ---
    for thisComponent in RecallPracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialFSPractice.addData('textboxPractice.text',textboxPractice.text)
    # Run 'End Routine' code from code_3practice
    #for r in range(len(digitsForTrial)):
    #    digitsForTrial[r] = str(digitsForTrial[r])
    
    #digitsForTrial = ''.join(digitsForTrial)
    
    if textboxPractice.text == str(digits):
        correct = 1
        fbTxt = 'Correct!'
    else:
        correct = 0
        fbTxt = 'Incorrect'
    thisExp.addData('correct', correct)
    # store data for trialFSPractice (TrialHandler)
    x, y = mousePractice.getPos()
    buttons = mousePractice.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter(cont_buttonPractice)
            clickableList = cont_buttonPractice
        except:
            clickableList = [cont_buttonPractice]
        for obj in clickableList:
            if obj.contains(mousePractice):
                gotValidClick = True
                mousePractice.clicked_name.append(obj.name)
    trialFSPractice.addData('mousePractice.x', x)
    trialFSPractice.addData('mousePractice.y', y)
    trialFSPractice.addData('mousePractice.leftButton', buttons[0])
    trialFSPractice.addData('mousePractice.midButton', buttons[1])
    trialFSPractice.addData('mousePractice.rightButton', buttons[2])
    if len(mousePractice.clicked_name):
        trialFSPractice.addData('mousePractice.clicked_name', mousePractice.clicked_name[0])
    # the Routine "RecallPractice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "FeedbackPractice" ---
    continueRoutine = True
    # update component parameters for each repeat
    feedbac_textPractice.setText(fbTxt)
    # keep track of which components have finished
    FeedbackPracticeComponents = [feedbac_textPractice]
    for thisComponent in FeedbackPracticeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "FeedbackPractice" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedbac_textPractice* updates
        if feedbac_textPractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedbac_textPractice.frameNStart = frameN  # exact frame index
            feedbac_textPractice.tStart = t  # local t and not account for scr refresh
            feedbac_textPractice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedbac_textPractice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedbac_textPractice.started')
            feedbac_textPractice.setAutoDraw(True)
        if feedbac_textPractice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedbac_textPractice.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                feedbac_textPractice.tStop = t  # not accounting for scr refresh
                feedbac_textPractice.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedbac_textPractice.stopped')
                feedbac_textPractice.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackPracticeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "FeedbackPractice" ---
    for thisComponent in FeedbackPracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialFSPractice'


# --- Prepare to start Routine "StartRealFS" ---
continueRoutine = True
# update component parameters for each repeat
startFSreal.keys = []
startFSreal.rt = []
_startFSreal_allKeys = []
# keep track of which components have finished
StartRealFSComponents = [praccomplete, startFSreal]
for thisComponent in StartRealFSComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "StartRealFS" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *praccomplete* updates
    if praccomplete.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        praccomplete.frameNStart = frameN  # exact frame index
        praccomplete.tStart = t  # local t and not account for scr refresh
        praccomplete.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(praccomplete, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'praccomplete.started')
        praccomplete.setAutoDraw(True)
    
    # *startFSreal* updates
    waitOnFlip = False
    if startFSreal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        startFSreal.frameNStart = frameN  # exact frame index
        startFSreal.tStart = t  # local t and not account for scr refresh
        startFSreal.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(startFSreal, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'startFSreal.started')
        startFSreal.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(startFSreal.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(startFSreal.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if startFSreal.status == STARTED and not waitOnFlip:
        theseKeys = startFSreal.getKeys(keyList=['return'], waitRelease=False)
        _startFSreal_allKeys.extend(theseKeys)
        if len(_startFSreal_allKeys):
            startFSreal.keys = _startFSreal_allKeys[-1].name  # just the last key pressed
            startFSreal.rt = _startFSreal_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartRealFSComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "StartRealFS" ---
for thisComponent in StartRealFSComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if startFSreal.keys in ['', [], None]:  # No response was made
    startFSreal.keys = None
thisExp.addData('startFSreal.keys',startFSreal.keys)
if startFSreal.keys != None:  # we had a response
    thisExp.addData('startFSreal.rt', startFSreal.rt)
thisExp.nextEntry()
# the Routine "StartRealFS" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialsFS = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('digitSpanTrialNumber.xlsx'),
    seed=None, name='trialsFS')
thisExp.addLoop(trialsFS)  # add the loop to the experiment
thisTrialsFS = trialsFS.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsFS.rgb)
if thisTrialsFS != None:
    for paramName in thisTrialsFS:
        exec('{} = thisTrialsFS[paramName]'.format(paramName))

for thisTrialsFS in trialsFS:
    currentLoop = trialsFS
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsFS.rgb)
    if thisTrialsFS != None:
        for paramName in thisTrialsFS:
            exec('{} = thisTrialsFS[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "selectNumbers" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from selectNumbersFS
    import random
    
    nTrialsFS += 1;
    
    # set the digit span, always starts at 3 for nTrial =1
    # if correct, go up one
    # if incorrect (once) stay the same
    # if incorrect (twice) go down one
    if correct == 0:
        incorrectCount += 1
    
    if nTrialsFS ==1:
        digitSpan = minDigitFS
    else:
        if correct ==1:
            digitSpan = digitSpan + 1
            incorrectCount = 0;
        elif correct ==0 and incorrectCount <2:
            digitSpan = digitSpan
        elif correct ==0 and incorrectCount ==2:
            digitSpan = digitSpan-1
            incorrectCount = 0;
    
    if digitSpan < minDigitFS:
        digitSpan = minDigitFS
    
    digitsForTrial = [];
    
    while len(digitsForTrial) < digitSpan:
        if digitSpan <= 9:
            singleNumber = random.choice(numbersToChoose)
            if digitsForTrial.count(singleNumber) < 1:
                digitsForTrial.append(singleNumber)        
        elif digitSpan > 9:
             singleNumber = random.choice(numbersToChoose)
            
             if len(digitsForTrial) < 9 and digitsForTrial.count(singleNumber)==0:
                 digitsForTrial.append(singleNumber)
            
             if len(digitsForTrial) >= 9 and digitsForTrial.count(singleNumber)<2:
                 digitsForTrial.append(singleNumber)
                 
    # check that there is not more than two consecutive numbers (e.g. 1-2-3)
    checkingNumbers = True
    startN = 1
    endN = len(digitsForTrial)-1
    while checkingNumbers:
        for n in range(startN,endN):
            if digitsForTrial[n] == digitsForTrial[n-1] + 1 and digitsForTrial[n] == digitsForTrial[n+1] -1:
                tmpFirst = digitsForTrial[n]
                tmpSecond = digitsForTrial[n-1]
                digitsForTrial[n] = tmpSecond
                digitsForTrial[n-1] = tmpFirst
            
            if digitsForTrial[n] == digitsForTrial[n-1] - 1 and digitsForTrial[n] == digitsForTrial[n+1] +1:
                tmpFirst = digitsForTrial[n]
                tmpSecond = digitsForTrial[n-1]
                digitsForTrial[n] = tmpSecond
                digitsForTrial[n-1] = tmpFirst
                
        checkingNumbers = False
    # if there are three consecutive numbers, swap the first and second numbers in the series
    # keep track of which components have finished
    selectNumbersComponents = []
    for thisComponent in selectNumbersComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "selectNumbers" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in selectNumbersComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "selectNumbers" ---
    for thisComponent in selectNumbersComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "selectNumbers" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    digitLoop = data.TrialHandler(nReps=digitSpan, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='digitLoop')
    thisExp.addLoop(digitLoop)  # add the loop to the experiment
    thisDigitLoop = digitLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisDigitLoop.rgb)
    if thisDigitLoop != None:
        for paramName in thisDigitLoop:
            exec('{} = thisDigitLoop[paramName]'.format(paramName))
    
    for thisDigitLoop in digitLoop:
        currentLoop = digitLoop
        # abbreviate parameter names if possible (e.g. rgb = thisDigitLoop.rgb)
        if thisDigitLoop != None:
            for paramName in thisDigitLoop:
                exec('{} = thisDigitLoop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "ShowNumbers" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from getTmpNumberCodeFS
        tmpNumber = digitsForTrial[digitLoop.thisN]
        presentation_text.setText(tmpNumber)
        # keep track of which components have finished
        ShowNumbersComponents = [fixation, presentation_text]
        for thisComponent in ShowNumbersComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ShowNumbers" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation* updates
            if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation.started')
                fixation.setAutoDraw(True)
            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation.stopped')
                    fixation.setAutoDraw(False)
            
            # *presentation_text* updates
            if presentation_text.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                presentation_text.frameNStart = frameN  # exact frame index
                presentation_text.tStart = t  # local t and not account for scr refresh
                presentation_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(presentation_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'presentation_text.started')
                presentation_text.setAutoDraw(True)
            if presentation_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > presentation_text.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    presentation_text.tStop = t  # not accounting for scr refresh
                    presentation_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'presentation_text.stopped')
                    presentation_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ShowNumbersComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ShowNumbers" ---
        for thisComponent in ShowNumbersComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from getTmpNumberCodeFS
        thisExp.addData("digitsForTrial",digitsForTrial)
        # using non-slip timing so subtract the expected duration of this Routine
        routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
    # completed digitSpan repeats of 'digitLoop'
    
    
    # --- Prepare to start Routine "Recall" ---
    continueRoutine = True
    # update component parameters for each repeat
    textbox.reset()
    # setup some python lists for storing info about the mouse_3
    mouse_3.clicked_name = []
    gotValidClick = False  # until a click is received
    # Run 'Begin Routine' code from JScode
    # translated from js
    # this is a temporary fix to allow editable textbox to be used on several trials
    #textboxPractice.refresh()
    # keep track of which components have finished
    RecallComponents = [recall_txt, textbox, cont_button, mouse_3]
    for thisComponent in RecallComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Recall" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *recall_txt* updates
        if recall_txt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            recall_txt.frameNStart = frameN  # exact frame index
            recall_txt.tStart = t  # local t and not account for scr refresh
            recall_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recall_txt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'recall_txt.started')
            recall_txt.setAutoDraw(True)
        
        # *textbox* updates
        if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textbox.frameNStart = frameN  # exact frame index
            textbox.tStart = t  # local t and not account for scr refresh
            textbox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textbox.started')
            textbox.setAutoDraw(True)
        
        # *cont_button* updates
        if cont_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cont_button.frameNStart = frameN  # exact frame index
            cont_button.tStart = t  # local t and not account for scr refresh
            cont_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cont_button, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cont_button.started')
            cont_button.setAutoDraw(True)
        # *mouse_3* updates
        if mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_3.frameNStart = frameN  # exact frame index
            mouse_3.tStart = t  # local t and not account for scr refresh
            mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_3.started', t)
            mouse_3.status = STARTED
            mouse_3.mouseClock.reset()
            prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
        if mouse_3.status == STARTED:  # only update if started and not finished!
            buttons = mouse_3.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(cont_button)
                        clickableList = cont_button
                    except:
                        clickableList = [cont_button]
                    for obj in clickableList:
                        if obj.contains(mouse_3):
                            gotValidClick = True
                            mouse_3.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RecallComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Recall" ---
    for thisComponent in RecallComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialsFS.addData('textbox.text',textbox.text)
    # Run 'End Routine' code from code_3
    for r in range(len(digitsForTrial)):
        digitsForTrial[r] = str(digitsForTrial[r])
    
    digitsForTrial = ''.join(digitsForTrial)
    
    if textbox.text == str(digitsForTrial):
        correct = 1
        fbTxt = 'Correct!'
    else:
        correct = 0
        fbTxt = 'Incorrect'
    thisExp.addData('correct', correct)
    # store data for trialsFS (TrialHandler)
    x, y = mouse_3.getPos()
    buttons = mouse_3.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter(cont_button)
            clickableList = cont_button
        except:
            clickableList = [cont_button]
        for obj in clickableList:
            if obj.contains(mouse_3):
                gotValidClick = True
                mouse_3.clicked_name.append(obj.name)
    trialsFS.addData('mouse_3.x', x)
    trialsFS.addData('mouse_3.y', y)
    trialsFS.addData('mouse_3.leftButton', buttons[0])
    trialsFS.addData('mouse_3.midButton', buttons[1])
    trialsFS.addData('mouse_3.rightButton', buttons[2])
    if len(mouse_3.clicked_name):
        trialsFS.addData('mouse_3.clicked_name', mouse_3.clicked_name[0])
    # the Routine "Recall" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Feedback" ---
    continueRoutine = True
    # update component parameters for each repeat
    feedback_text.setText(fbTxt)
    # keep track of which components have finished
    FeedbackComponents = [feedback_text]
    for thisComponent in FeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Feedback" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_text* updates
        if feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_text.frameNStart = frameN  # exact frame index
            feedback_text.tStart = t  # local t and not account for scr refresh
            feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_text.started')
            feedback_text.setAutoDraw(True)
        if feedback_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_text.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                feedback_text.tStop = t  # not accounting for scr refresh
                feedback_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_text.stopped')
                feedback_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Feedback" ---
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialsFS'


# --- Prepare to start Routine "FStoBStransition" ---
continueRoutine = True
# update component parameters for each repeat
moveToBS.keys = []
moveToBS.rt = []
_moveToBS_allKeys = []
# keep track of which components have finished
FStoBStransitionComponents = [roundTransition, moveToBS]
for thisComponent in FStoBStransitionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "FStoBStransition" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *roundTransition* updates
    if roundTransition.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        roundTransition.frameNStart = frameN  # exact frame index
        roundTransition.tStart = t  # local t and not account for scr refresh
        roundTransition.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(roundTransition, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'roundTransition.started')
        roundTransition.setAutoDraw(True)
    
    # *moveToBS* updates
    waitOnFlip = False
    if moveToBS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        moveToBS.frameNStart = frameN  # exact frame index
        moveToBS.tStart = t  # local t and not account for scr refresh
        moveToBS.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(moveToBS, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'moveToBS.started')
        moveToBS.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(moveToBS.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(moveToBS.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if moveToBS.status == STARTED and not waitOnFlip:
        theseKeys = moveToBS.getKeys(keyList=['return'], waitRelease=False)
        _moveToBS_allKeys.extend(theseKeys)
        if len(_moveToBS_allKeys):
            moveToBS.keys = _moveToBS_allKeys[-1].name  # just the last key pressed
            moveToBS.rt = _moveToBS_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FStoBStransitionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "FStoBStransition" ---
for thisComponent in FStoBStransitionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if moveToBS.keys in ['', [], None]:  # No response was made
    moveToBS.keys = None
thisExp.addData('moveToBS.keys',moveToBS.keys)
if moveToBS.keys != None:  # we had a response
    thisExp.addData('moveToBS.rt', moveToBS.rt)
thisExp.nextEntry()
# the Routine "FStoBStransition" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "InstructionsBS" ---
continueRoutine = True
# update component parameters for each repeat
startBSprac.keys = []
startBSprac.rt = []
_startBSprac_allKeys = []
# keep track of which components have finished
InstructionsBSComponents = [BSGenInsText, startBSprac]
for thisComponent in InstructionsBSComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "InstructionsBS" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *BSGenInsText* updates
    if BSGenInsText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BSGenInsText.frameNStart = frameN  # exact frame index
        BSGenInsText.tStart = t  # local t and not account for scr refresh
        BSGenInsText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BSGenInsText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'BSGenInsText.started')
        BSGenInsText.setAutoDraw(True)
    
    # *startBSprac* updates
    waitOnFlip = False
    if startBSprac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        startBSprac.frameNStart = frameN  # exact frame index
        startBSprac.tStart = t  # local t and not account for scr refresh
        startBSprac.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(startBSprac, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'startBSprac.started')
        startBSprac.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(startBSprac.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(startBSprac.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if startBSprac.status == STARTED and not waitOnFlip:
        theseKeys = startBSprac.getKeys(keyList=['return'], waitRelease=False)
        _startBSprac_allKeys.extend(theseKeys)
        if len(_startBSprac_allKeys):
            startBSprac.keys = _startBSprac_allKeys[-1].name  # just the last key pressed
            startBSprac.rt = _startBSprac_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsBSComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "InstructionsBS" ---
for thisComponent in InstructionsBSComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if startBSprac.keys in ['', [], None]:  # No response was made
    startBSprac.keys = None
thisExp.addData('startBSprac.keys',startBSprac.keys)
if startBSprac.keys != None:  # we had a response
    thisExp.addData('startBSprac.rt', startBSprac.rt)
thisExp.nextEntry()
# the Routine "InstructionsBS" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialsPracticeBS = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('digitSpanPractice.xlsx'),
    seed=None, name='trialsPracticeBS')
thisExp.addLoop(trialsPracticeBS)  # add the loop to the experiment
thisTrialsPracticeBS = trialsPracticeBS.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsPracticeBS.rgb)
if thisTrialsPracticeBS != None:
    for paramName in thisTrialsPracticeBS:
        exec('{} = thisTrialsPracticeBS[paramName]'.format(paramName))

for thisTrialsPracticeBS in trialsPracticeBS:
    currentLoop = trialsPracticeBS
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsPracticeBS.rgb)
    if thisTrialsPracticeBS != None:
        for paramName in thisTrialsPracticeBS:
            exec('{} = thisTrialsPracticeBS[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    digitLoopPracticeBS = data.TrialHandler(nReps=2.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='digitLoopPracticeBS')
    thisExp.addLoop(digitLoopPracticeBS)  # add the loop to the experiment
    thisDigitLoopPracticeBS = digitLoopPracticeBS.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisDigitLoopPracticeBS.rgb)
    if thisDigitLoopPracticeBS != None:
        for paramName in thisDigitLoopPracticeBS:
            exec('{} = thisDigitLoopPracticeBS[paramName]'.format(paramName))
    
    for thisDigitLoopPracticeBS in digitLoopPracticeBS:
        currentLoop = digitLoopPracticeBS
        # abbreviate parameter names if possible (e.g. rgb = thisDigitLoopPracticeBS.rgb)
        if thisDigitLoopPracticeBS != None:
            for paramName in thisDigitLoopPracticeBS:
                exec('{} = thisDigitLoopPracticeBS[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "showNumbersPracticeBS" ---
        continueRoutine = True
        # update component parameters for each repeat
        pres_text_practice_2.setText(str(digitsReverse)[digitLoopPracticeBS.thisN])
        # keep track of which components have finished
        showNumbersPracticeBSComponents = [fixation_3, pres_text_practice_2]
        for thisComponent in showNumbersPracticeBSComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "showNumbersPracticeBS" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_3* updates
            if fixation_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_3.frameNStart = frameN  # exact frame index
                fixation_3.tStart = t  # local t and not account for scr refresh
                fixation_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_3.started')
                fixation_3.setAutoDraw(True)
            if fixation_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_3.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_3.tStop = t  # not accounting for scr refresh
                    fixation_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_3.stopped')
                    fixation_3.setAutoDraw(False)
            
            # *pres_text_practice_2* updates
            if pres_text_practice_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                pres_text_practice_2.frameNStart = frameN  # exact frame index
                pres_text_practice_2.tStart = t  # local t and not account for scr refresh
                pres_text_practice_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pres_text_practice_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pres_text_practice_2.started')
                pres_text_practice_2.setAutoDraw(True)
            if pres_text_practice_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > pres_text_practice_2.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    pres_text_practice_2.tStop = t  # not accounting for scr refresh
                    pres_text_practice_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'pres_text_practice_2.stopped')
                    pres_text_practice_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in showNumbersPracticeBSComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "showNumbersPracticeBS" ---
        for thisComponent in showNumbersPracticeBSComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine
        routineTimer.addTime(-2.000000)
    # completed 2.0 repeats of 'digitLoopPracticeBS'
    
    
    # --- Prepare to start Routine "recallPracticeBS" ---
    continueRoutine = True
    # update component parameters for each repeat
    textboxPractice_2.reset()
    # setup some python lists for storing info about the mousePractice_2
    mousePractice_2.clicked_name = []
    gotValidClick = False  # until a click is received
    # Run 'Begin Routine' code from JScodePractice_2
    # translated from js
    # this is a temporary fix to allow editable textbox to be used on several trials
    #textboxPractice.refresh()
    # keep track of which components have finished
    recallPracticeBSComponents = [recall_txtPractice_2, textboxPractice_2, cont_buttonPractice_2, mousePractice_2]
    for thisComponent in recallPracticeBSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "recallPracticeBS" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *recall_txtPractice_2* updates
        if recall_txtPractice_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            recall_txtPractice_2.frameNStart = frameN  # exact frame index
            recall_txtPractice_2.tStart = t  # local t and not account for scr refresh
            recall_txtPractice_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recall_txtPractice_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'recall_txtPractice_2.started')
            recall_txtPractice_2.setAutoDraw(True)
        
        # *textboxPractice_2* updates
        if textboxPractice_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textboxPractice_2.frameNStart = frameN  # exact frame index
            textboxPractice_2.tStart = t  # local t and not account for scr refresh
            textboxPractice_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textboxPractice_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textboxPractice_2.started')
            textboxPractice_2.setAutoDraw(True)
        
        # *cont_buttonPractice_2* updates
        if cont_buttonPractice_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cont_buttonPractice_2.frameNStart = frameN  # exact frame index
            cont_buttonPractice_2.tStart = t  # local t and not account for scr refresh
            cont_buttonPractice_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cont_buttonPractice_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cont_buttonPractice_2.started')
            cont_buttonPractice_2.setAutoDraw(True)
        # *mousePractice_2* updates
        if mousePractice_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mousePractice_2.frameNStart = frameN  # exact frame index
            mousePractice_2.tStart = t  # local t and not account for scr refresh
            mousePractice_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mousePractice_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mousePractice_2.started', t)
            mousePractice_2.status = STARTED
            mousePractice_2.mouseClock.reset()
            prevButtonState = mousePractice_2.getPressed()  # if button is down already this ISN'T a new click
        if mousePractice_2.status == STARTED:  # only update if started and not finished!
            buttons = mousePractice_2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(cont_buttonPractice_2)
                        clickableList = cont_buttonPractice_2
                    except:
                        clickableList = [cont_buttonPractice_2]
                    for obj in clickableList:
                        if obj.contains(mousePractice_2):
                            gotValidClick = True
                            mousePractice_2.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in recallPracticeBSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "recallPracticeBS" ---
    for thisComponent in recallPracticeBSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialsPracticeBS.addData('textboxPractice_2.text',textboxPractice_2.text)
    # Run 'End Routine' code from code_3practice_2
    if textboxPractice_2.text == str(digitsReverseCorrAnswer):
        correct = 1
        fbTxt = 'Correct!'
    else:
        correct = 0
        fbTxt = 'Incorrect'
    thisExp.addData('correct', correct)
    # store data for trialsPracticeBS (TrialHandler)
    x, y = mousePractice_2.getPos()
    buttons = mousePractice_2.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter(cont_buttonPractice_2)
            clickableList = cont_buttonPractice_2
        except:
            clickableList = [cont_buttonPractice_2]
        for obj in clickableList:
            if obj.contains(mousePractice_2):
                gotValidClick = True
                mousePractice_2.clicked_name.append(obj.name)
    trialsPracticeBS.addData('mousePractice_2.x', x)
    trialsPracticeBS.addData('mousePractice_2.y', y)
    trialsPracticeBS.addData('mousePractice_2.leftButton', buttons[0])
    trialsPracticeBS.addData('mousePractice_2.midButton', buttons[1])
    trialsPracticeBS.addData('mousePractice_2.rightButton', buttons[2])
    if len(mousePractice_2.clicked_name):
        trialsPracticeBS.addData('mousePractice_2.clicked_name', mousePractice_2.clicked_name[0])
    # the Routine "recallPracticeBS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedbackPracticeBS" ---
    continueRoutine = True
    # update component parameters for each repeat
    feedbac_textPractice_2.setText(fbTxt)
    # keep track of which components have finished
    feedbackPracticeBSComponents = [feedbac_textPractice_2]
    for thisComponent in feedbackPracticeBSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "feedbackPracticeBS" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedbac_textPractice_2* updates
        if feedbac_textPractice_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedbac_textPractice_2.frameNStart = frameN  # exact frame index
            feedbac_textPractice_2.tStart = t  # local t and not account for scr refresh
            feedbac_textPractice_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedbac_textPractice_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedbac_textPractice_2.started')
            feedbac_textPractice_2.setAutoDraw(True)
        if feedbac_textPractice_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedbac_textPractice_2.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                feedbac_textPractice_2.tStop = t  # not accounting for scr refresh
                feedbac_textPractice_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedbac_textPractice_2.stopped')
                feedbac_textPractice_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackPracticeBSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedbackPracticeBS" ---
    for thisComponent in feedbackPracticeBSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialsPracticeBS'


# --- Prepare to start Routine "startRealBS" ---
continueRoutine = True
# update component parameters for each repeat
startBSreal.keys = []
startBSreal.rt = []
_startBSreal_allKeys = []
# keep track of which components have finished
startRealBSComponents = [praccompleteBS, startBSreal]
for thisComponent in startRealBSComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "startRealBS" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *praccompleteBS* updates
    if praccompleteBS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        praccompleteBS.frameNStart = frameN  # exact frame index
        praccompleteBS.tStart = t  # local t and not account for scr refresh
        praccompleteBS.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(praccompleteBS, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'praccompleteBS.started')
        praccompleteBS.setAutoDraw(True)
    
    # *startBSreal* updates
    waitOnFlip = False
    if startBSreal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        startBSreal.frameNStart = frameN  # exact frame index
        startBSreal.tStart = t  # local t and not account for scr refresh
        startBSreal.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(startBSreal, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'startBSreal.started')
        startBSreal.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(startBSreal.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(startBSreal.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if startBSreal.status == STARTED and not waitOnFlip:
        theseKeys = startBSreal.getKeys(keyList=['return'], waitRelease=False)
        _startBSreal_allKeys.extend(theseKeys)
        if len(_startBSreal_allKeys):
            startBSreal.keys = _startBSreal_allKeys[-1].name  # just the last key pressed
            startBSreal.rt = _startBSreal_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startRealBSComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "startRealBS" ---
for thisComponent in startRealBSComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if startBSreal.keys in ['', [], None]:  # No response was made
    startBSreal.keys = None
thisExp.addData('startBSreal.keys',startBSreal.keys)
if startBSreal.keys != None:  # we had a response
    thisExp.addData('startBSreal.rt', startBSreal.rt)
thisExp.nextEntry()
# the Routine "startRealBS" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialsBS = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('digitSpanTrialNumber.xlsx'),
    seed=None, name='trialsBS')
thisExp.addLoop(trialsBS)  # add the loop to the experiment
thisTrialsBS = trialsBS.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsBS.rgb)
if thisTrialsBS != None:
    for paramName in thisTrialsBS:
        exec('{} = thisTrialsBS[paramName]'.format(paramName))

for thisTrialsBS in trialsBS:
    currentLoop = trialsBS
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsBS.rgb)
    if thisTrialsBS != None:
        for paramName in thisTrialsBS:
            exec('{} = thisTrialsBS[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "selectNumbersBS" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from selectNumbersBScode
    import random
    
    nTrialsBS += 1;
    
    # set the digit span, always starts at 3 for nTrial =1
    # if correct, go up one
    # if incorrect (once) stay the same
    # if incorrect (twice) go down one
    if correct == 0:
        incorrectCount += 1
    
    if nTrialsBS ==1:
        correct = [];
        digitSpan = minDigitBS
    else:
        if correct ==1:
            digitSpan = digitSpan + 1
            incorrectCount = 0;
        elif correct ==0 and incorrectCount <2:
            digitSpan = digitSpan
        elif correct ==0 and incorrectCount ==2:
            digitSpan = digitSpan-1
            incorrectCount = 0;
    
    if digitSpan < minDigitBS:
        digitSpan = minDigitBS
    
    digitsForTrial = [];
    
    while len(digitsForTrial) < digitSpan:
        if digitSpan <= 9:
            singleNumber = random.choice(numbersToChoose)
            if digitsForTrial.count(singleNumber) < 1:
                digitsForTrial.append(singleNumber)        
        elif digitSpan > 9:
             singleNumber = random.choice(numbersToChoose)
            
             if len(digitsForTrial) < 9 and digitsForTrial.count(singleNumber)==0:
                 digitsForTrial.append(singleNumber)
            
             if len(digitsForTrial) >= 9 and digitsForTrial.count(singleNumber)<2:
                 digitsForTrial.append(singleNumber)
                 
    # check that there is not more than two consecutive numbers (e.g. 1-2-3)
    checkingNumbers = True
    startN = 1
    endN = len(digitsForTrial)-1
    while checkingNumbers:
        for n in range(startN,endN):
            if digitsForTrial[n] == digitsForTrial[n-1] + 1 and digitsForTrial[n] == digitsForTrial[n+1] -1:
                tmpFirst = digitsForTrial[n]
                tmpSecond = digitsForTrial[n-1]
                digitsForTrial[n] = tmpSecond
                digitsForTrial[n-1] = tmpFirst
            
            if digitsForTrial[n] == digitsForTrial[n-1] - 1 and digitsForTrial[n] == digitsForTrial[n+1] +1:
                tmpFirst = digitsForTrial[n]
                tmpSecond = digitsForTrial[n-1]
                digitsForTrial[n] = tmpSecond
                digitsForTrial[n-1] = tmpFirst
                
        checkingNumbers = False
    # if there are three consecutive numbers, swap the first and second numbers in the series
    # keep track of which components have finished
    selectNumbersBSComponents = []
    for thisComponent in selectNumbersBSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "selectNumbersBS" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in selectNumbersBSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "selectNumbersBS" ---
    for thisComponent in selectNumbersBSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "selectNumbersBS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    digitLoopBS = data.TrialHandler(nReps=digitSpan, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='digitLoopBS')
    thisExp.addLoop(digitLoopBS)  # add the loop to the experiment
    thisDigitLoopBS = digitLoopBS.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisDigitLoopBS.rgb)
    if thisDigitLoopBS != None:
        for paramName in thisDigitLoopBS:
            exec('{} = thisDigitLoopBS[paramName]'.format(paramName))
    
    for thisDigitLoopBS in digitLoopBS:
        currentLoop = digitLoopBS
        # abbreviate parameter names if possible (e.g. rgb = thisDigitLoopBS.rgb)
        if thisDigitLoopBS != None:
            for paramName in thisDigitLoopBS:
                exec('{} = thisDigitLoopBS[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "showNumbersBS" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from getTmpNumberCodeBS
        tmpNumber = digitsForTrial[digitLoopBS.thisN]
        presentation_textBS.setText(tmpNumber)
        # keep track of which components have finished
        showNumbersBSComponents = [fixationBS, presentation_textBS]
        for thisComponent in showNumbersBSComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "showNumbersBS" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixationBS* updates
            if fixationBS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixationBS.frameNStart = frameN  # exact frame index
                fixationBS.tStart = t  # local t and not account for scr refresh
                fixationBS.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixationBS, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixationBS.started')
                fixationBS.setAutoDraw(True)
            if fixationBS.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixationBS.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixationBS.tStop = t  # not accounting for scr refresh
                    fixationBS.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixationBS.stopped')
                    fixationBS.setAutoDraw(False)
            
            # *presentation_textBS* updates
            if presentation_textBS.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                presentation_textBS.frameNStart = frameN  # exact frame index
                presentation_textBS.tStart = t  # local t and not account for scr refresh
                presentation_textBS.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(presentation_textBS, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'presentation_textBS.started')
                presentation_textBS.setAutoDraw(True)
            if presentation_textBS.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > presentation_textBS.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    presentation_textBS.tStop = t  # not accounting for scr refresh
                    presentation_textBS.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'presentation_textBS.stopped')
                    presentation_textBS.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in showNumbersBSComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "showNumbersBS" ---
        for thisComponent in showNumbersBSComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from getTmpNumberCodeBS
        thisExp.addData("digitsForTrial",digitsForTrial)
        # using non-slip timing so subtract the expected duration of this Routine
        routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
    # completed digitSpan repeats of 'digitLoopBS'
    
    
    # --- Prepare to start Routine "RecallBS" ---
    continueRoutine = True
    # update component parameters for each repeat
    textboxBS.reset()
    # setup some python lists for storing info about the mouseBS
    mouseBS.clicked_name = []
    gotValidClick = False  # until a click is received
    # Run 'Begin Routine' code from JScode_BS
    # translated from js
    # this is a temporary fix to allow editable textbox to be used on several trials
    #textboxPractice.refresh()
    # keep track of which components have finished
    RecallBSComponents = [recall_txtBS, textboxBS, cont_buttonBS, mouseBS]
    for thisComponent in RecallBSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "RecallBS" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *recall_txtBS* updates
        if recall_txtBS.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            recall_txtBS.frameNStart = frameN  # exact frame index
            recall_txtBS.tStart = t  # local t and not account for scr refresh
            recall_txtBS.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recall_txtBS, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'recall_txtBS.started')
            recall_txtBS.setAutoDraw(True)
        
        # *textboxBS* updates
        if textboxBS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textboxBS.frameNStart = frameN  # exact frame index
            textboxBS.tStart = t  # local t and not account for scr refresh
            textboxBS.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textboxBS, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textboxBS.started')
            textboxBS.setAutoDraw(True)
        
        # *cont_buttonBS* updates
        if cont_buttonBS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cont_buttonBS.frameNStart = frameN  # exact frame index
            cont_buttonBS.tStart = t  # local t and not account for scr refresh
            cont_buttonBS.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cont_buttonBS, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cont_buttonBS.started')
            cont_buttonBS.setAutoDraw(True)
        # *mouseBS* updates
        if mouseBS.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouseBS.frameNStart = frameN  # exact frame index
            mouseBS.tStart = t  # local t and not account for scr refresh
            mouseBS.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouseBS, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouseBS.started', t)
            mouseBS.status = STARTED
            mouseBS.mouseClock.reset()
            prevButtonState = mouseBS.getPressed()  # if button is down already this ISN'T a new click
        if mouseBS.status == STARTED:  # only update if started and not finished!
            buttons = mouseBS.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(cont_buttonBS)
                        clickableList = cont_buttonBS
                    except:
                        clickableList = [cont_buttonBS]
                    for obj in clickableList:
                        if obj.contains(mouseBS):
                            gotValidClick = True
                            mouseBS.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RecallBSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "RecallBS" ---
    for thisComponent in RecallBSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialsBS.addData('textboxBS.text',textboxBS.text)
    # Run 'End Routine' code from code_3BS
    digitsForTrial.reverse(); # reverse order for backward span
    
    for r in range(len(digitsForTrial)):
        digitsForTrial[r] = str(digitsForTrial[r])
    
    digitsForTrial = ''.join(digitsForTrial)
    
    if textboxBS.text == str(digitsForTrial):
        correct = 1
        fbTxt = 'Correct!'
    else:
        correct = 0
        fbTxt = 'Incorrect'
    thisExp.addData('correct', correct)
    # store data for trialsBS (TrialHandler)
    x, y = mouseBS.getPos()
    buttons = mouseBS.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter(cont_buttonBS)
            clickableList = cont_buttonBS
        except:
            clickableList = [cont_buttonBS]
        for obj in clickableList:
            if obj.contains(mouseBS):
                gotValidClick = True
                mouseBS.clicked_name.append(obj.name)
    trialsBS.addData('mouseBS.x', x)
    trialsBS.addData('mouseBS.y', y)
    trialsBS.addData('mouseBS.leftButton', buttons[0])
    trialsBS.addData('mouseBS.midButton', buttons[1])
    trialsBS.addData('mouseBS.rightButton', buttons[2])
    if len(mouseBS.clicked_name):
        trialsBS.addData('mouseBS.clicked_name', mouseBS.clicked_name[0])
    # the Routine "RecallBS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "FeedbackBS" ---
    continueRoutine = True
    # update component parameters for each repeat
    feedback_textBS.setText(fbTxt)
    # keep track of which components have finished
    FeedbackBSComponents = [feedback_textBS]
    for thisComponent in FeedbackBSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "FeedbackBS" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_textBS* updates
        if feedback_textBS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_textBS.frameNStart = frameN  # exact frame index
            feedback_textBS.tStart = t  # local t and not account for scr refresh
            feedback_textBS.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_textBS, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_textBS.started')
            feedback_textBS.setAutoDraw(True)
        if feedback_textBS.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_textBS.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                feedback_textBS.tStop = t  # not accounting for scr refresh
                feedback_textBS.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_textBS.stopped')
                feedback_textBS.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackBSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "FeedbackBS" ---
    for thisComponent in FeedbackBSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialsBS'


# --- Prepare to start Routine "END" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
ENDComponents = [ThankYou]
for thisComponent in ENDComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "END" ---
while continueRoutine and routineTimer.getTime() < 2.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ThankYou* updates
    if ThankYou.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ThankYou.frameNStart = frameN  # exact frame index
        ThankYou.tStart = t  # local t and not account for scr refresh
        ThankYou.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ThankYou, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ThankYou.started')
        ThankYou.setAutoDraw(True)
    if ThankYou.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > ThankYou.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            ThankYou.tStop = t  # not accounting for scr refresh
            ThankYou.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ThankYou.stopped')
            ThankYou.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ENDComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "END" ---
for thisComponent in ENDComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine
routineTimer.addTime(-2.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
