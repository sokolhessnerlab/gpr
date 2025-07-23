#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on Thu Jul 10 13:27:37 2025
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
import psychopy
print(psychopy.__version__)
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'digitSpan_shlab'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = (1024, 768)
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/justinblake/Documents/GitHub/gpr/2_tasks/working_files/rcs_task_folder/cgt_digitSpan/digitSpan_shlab.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('exp')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=True,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "rdmToSpanTransition" ---
    
    # --- Initialize components for Routine "spanGeneralInstructions" ---
    GenInsText = visual.TextStim(win=win, name='GenInsText',
        text='In this task you will be asked to memorize a series of numbers and recall them. You will do this twice, once recalling the numbers as they are presented on the screen and once recalling the numbers in the reverse order presented on the screen. \n\nThere are 14 trials in each direction for a total of 28 trials. Click the continue button when you are ready. ',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    mouse_2 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_2.mouseClock = core.Clock()
    cont_buttonGEN = visual.ImageStim(
        win=win,
        name='cont_buttonGEN', 
        image='continue copy.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -.4), draggable=False, size=(0.3, 0.07),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "FSinstructions" ---
    FSGenInsText = visual.TextStim(win=win, name='FSGenInsText',
        text='You are about to begin the forwards section of this task. \n\nYou will start with a list of 3 numbers. If you are able to correctly recall two out of three lists you will proceed to longer list trials. \n\nType out your answer when "Recall" screen appears using the numbers at the top of the keyboard to type out the numbers in the order they were presented on the screen. \n\nIf you make a mistake you can use backspace to correct it.  Do not use spaces. Feedback will be provided.\n\nClick the continue button to begin a few practice trials.',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    FSMouse = event.Mouse(win=win)
    x, y = [None, None]
    FSMouse.mouseClock = core.Clock()
    cont_buttonFSIns = visual.ImageStim(
        win=win,
        name='cont_buttonFSIns', 
        image='continue copy.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -.4), draggable=False, size=(0.3, 0.07),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "showNumbersPractice" ---
    fixation_2 = visual.TextStim(win=win, name='fixation_2',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    pres_text_practice = visual.TextStim(win=win, name='pres_text_practice',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "recallPractice" ---
    recall_txtPractice = visual.TextStim(win=win, name='recall_txtPractice',
        text='Recall',
        font='Arial',
        pos=(0, 0.25), draggable=False, height=0.05, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    textboxPractice = visual.TextBox2(
         win, text=None, placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.1,
         size=(None, None), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='textboxPractice',
         depth=-1, autoLog=True,
    )
    cont_buttonPractice = visual.ImageStim(
        win=win,
        name='cont_buttonPractice', 
        image='continue copy.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -.4), draggable=False, size=(0.3, 0.07),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    # Run 'Begin Experiment' code from code_3practice
    cont_button = []
    mousePractice = event.Mouse(win=win)
    x, y = [None, None]
    mousePractice.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "feedbackPractice" ---
    feedbac_textPractice = visual.TextStim(win=win, name='feedbac_textPractice',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "startRealFS" ---
    text = visual.TextStim(win=win, name='text',
        text='start FS',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
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
    
    
    # --- Initialize components for Routine "showNumbers" ---
    fixation = visual.TextStim(win=win, name='fixation',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    presentation_text = visual.TextStim(win=win, name='presentation_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "Recall" ---
    recall_txt = visual.TextStim(win=win, name='recall_txt',
        text='Recall',
        font='Arial',
        pos=(0, 0.25), draggable=False, height=0.05, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    textbox = visual.TextBox2(
         win, text=None, placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.1,
         size=(None, None), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='textbox',
         depth=-1, autoLog=True,
    )
    cont_button = visual.ImageStim(
        win=win,
        name='cont_button', 
        image='continue.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -.4), draggable=False, size=(0.3, 0.07),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "Feedback" ---
    feedback_text = visual.TextStim(win=win, name='feedback_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "instructionsBS" ---
    BSGenInsText = visual.TextStim(win=win, name='BSGenInsText',
        text='You are about to begin the backwards section of this task. \n\nYou will start with a list of 2 numbers. If you are able to correctly recall two out of three lists you will proceed to longer list trials. \n\nType out your answer when "Recall" screen appears using the numbers at the top of the keyboard making sure to type out the answers in the REVERSE order than they are presented on the screen. For example if you see 3,2,1 you should answer 1,2,3. \n\nIf you make a mistake you can use backspace to correct it. Do not use spaces. Feedback will be provided.\n\nClick the continue button to begin a few practice trials.',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    BSMouse = event.Mouse(win=win)
    x, y = [None, None]
    BSMouse.mouseClock = core.Clock()
    cont_buttonBSIns = visual.ImageStim(
        win=win,
        name='cont_buttonBSIns', 
        image='continue.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -.4), draggable=False, size=(0.3, 0.07),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "showNumbersPracticeBS_2" ---
    fixation_3 = visual.TextStim(win=win, name='fixation_3',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    pres_text_practice_2 = visual.TextStim(win=win, name='pres_text_practice_2',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "recallPracticeBS" ---
    recall_txtPractice_2 = visual.TextStim(win=win, name='recall_txtPractice_2',
        text='Recall',
        font='Arial',
        pos=(0, 0.25), draggable=False, height=0.05, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    textboxPractice_2 = visual.TextBox2(
         win, text=None, placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.1,
         size=(None, None), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='textboxPractice_2',
         depth=-1, autoLog=True,
    )
    cont_buttonPractice_2 = visual.ImageStim(
        win=win,
        name='cont_buttonPractice_2', 
        image='continue.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -.4), draggable=False, size=(0.3, 0.07),
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
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "startRealBS" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text='start real BS',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
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
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    presentation_textBS = visual.TextStim(win=win, name='presentation_textBS',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "RecallBS" ---
    recall_txtBS = visual.TextStim(win=win, name='recall_txtBS',
        text='Recall',
        font='Arial',
        pos=(0, 0.25), draggable=False, height=0.05, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    textboxBS = visual.TextBox2(
         win, text=None, placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.1,
         size=(None, None), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='textboxBS',
         depth=-1, autoLog=True,
    )
    cont_buttonBS = visual.ImageStim(
        win=win,
        name='cont_buttonBS', 
        image='continue.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -.4), draggable=False, size=(0.3, 0.07),
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
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "End" ---
    ThankYou = visual.TextStim(win=win, name='ThankYou',
        text='Thank you! You have sucessfully completed the second portion of this experiment. \n\nYou will now be automatically redirected to Qualtrics to take a breif end of task survey. ',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "rdmToSpanTransition" ---
    # create an object to store info about Routine rdmToSpanTransition
    rdmToSpanTransition = data.Routine(
        name='rdmToSpanTransition',
        components=[],
    )
    rdmToSpanTransition.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for rdmToSpanTransition
    rdmToSpanTransition.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    rdmToSpanTransition.tStart = globalClock.getTime(format='float')
    rdmToSpanTransition.status = STARTED
    thisExp.addData('rdmToSpanTransition.started', rdmToSpanTransition.tStart)
    rdmToSpanTransition.maxDuration = None
    # keep track of which components have finished
    rdmToSpanTransitionComponents = rdmToSpanTransition.components
    for thisComponent in rdmToSpanTransition.components:
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
    
    # --- Run Routine "rdmToSpanTransition" ---
    rdmToSpanTransition.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            rdmToSpanTransition.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rdmToSpanTransition.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "rdmToSpanTransition" ---
    for thisComponent in rdmToSpanTransition.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for rdmToSpanTransition
    rdmToSpanTransition.tStop = globalClock.getTime(format='float')
    rdmToSpanTransition.tStopRefresh = tThisFlipGlobal
    thisExp.addData('rdmToSpanTransition.stopped', rdmToSpanTransition.tStop)
    thisExp.nextEntry()
    # the Routine "rdmToSpanTransition" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "spanGeneralInstructions" ---
    # create an object to store info about Routine spanGeneralInstructions
    spanGeneralInstructions = data.Routine(
        name='spanGeneralInstructions',
        components=[GenInsText, mouse_2, cont_buttonGEN],
    )
    spanGeneralInstructions.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_2
    mouse_2.x = []
    mouse_2.y = []
    mouse_2.leftButton = []
    mouse_2.midButton = []
    mouse_2.rightButton = []
    mouse_2.time = []
    gotValidClick = False  # until a click is received
    # store start times for spanGeneralInstructions
    spanGeneralInstructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    spanGeneralInstructions.tStart = globalClock.getTime(format='float')
    spanGeneralInstructions.status = STARTED
    thisExp.addData('spanGeneralInstructions.started', spanGeneralInstructions.tStart)
    spanGeneralInstructions.maxDuration = None
    # keep track of which components have finished
    spanGeneralInstructionsComponents = spanGeneralInstructions.components
    for thisComponent in spanGeneralInstructions.components:
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
    
    # --- Run Routine "spanGeneralInstructions" ---
    spanGeneralInstructions.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *GenInsText* updates
        
        # if GenInsText is starting this frame...
        if GenInsText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            GenInsText.frameNStart = frameN  # exact frame index
            GenInsText.tStart = t  # local t and not account for scr refresh
            GenInsText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(GenInsText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'GenInsText.started')
            # update status
            GenInsText.status = STARTED
            GenInsText.setAutoDraw(True)
        
        # if GenInsText is active this frame...
        if GenInsText.status == STARTED:
            # update params
            pass
        # *mouse_2* updates
        
        # if mouse_2 is starting this frame...
        if mouse_2.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            mouse_2.frameNStart = frameN  # exact frame index
            mouse_2.tStart = t  # local t and not account for scr refresh
            mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_2.started', t)
            # update status
            mouse_2.status = STARTED
            mouse_2.mouseClock.reset()
            prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
        if mouse_2.status == STARTED:  # only update if started and not finished!
            buttons = mouse_2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    pass
                    x, y = mouse_2.getPos()
                    mouse_2.x.append(x)
                    mouse_2.y.append(y)
                    buttons = mouse_2.getPressed()
                    mouse_2.leftButton.append(buttons[0])
                    mouse_2.midButton.append(buttons[1])
                    mouse_2.rightButton.append(buttons[2])
                    mouse_2.time.append(mouse_2.mouseClock.getTime())
                    
                    continueRoutine = False  # end routine on response
        
        # *cont_buttonGEN* updates
        
        # if cont_buttonGEN is starting this frame...
        if cont_buttonGEN.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            cont_buttonGEN.frameNStart = frameN  # exact frame index
            cont_buttonGEN.tStart = t  # local t and not account for scr refresh
            cont_buttonGEN.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cont_buttonGEN, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cont_buttonGEN.started')
            # update status
            cont_buttonGEN.status = STARTED
            cont_buttonGEN.setAutoDraw(True)
        
        # if cont_buttonGEN is active this frame...
        if cont_buttonGEN.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            spanGeneralInstructions.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in spanGeneralInstructions.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "spanGeneralInstructions" ---
    for thisComponent in spanGeneralInstructions.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for spanGeneralInstructions
    spanGeneralInstructions.tStop = globalClock.getTime(format='float')
    spanGeneralInstructions.tStopRefresh = tThisFlipGlobal
    thisExp.addData('spanGeneralInstructions.stopped', spanGeneralInstructions.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_2.x', mouse_2.x)
    thisExp.addData('mouse_2.y', mouse_2.y)
    thisExp.addData('mouse_2.leftButton', mouse_2.leftButton)
    thisExp.addData('mouse_2.midButton', mouse_2.midButton)
    thisExp.addData('mouse_2.rightButton', mouse_2.rightButton)
    thisExp.addData('mouse_2.time', mouse_2.time)
    thisExp.nextEntry()
    # the Routine "spanGeneralInstructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "FSinstructions" ---
    # create an object to store info about Routine FSinstructions
    FSinstructions = data.Routine(
        name='FSinstructions',
        components=[FSGenInsText, FSMouse, cont_buttonFSIns],
    )
    FSinstructions.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the FSMouse
    FSMouse.x = []
    FSMouse.y = []
    FSMouse.leftButton = []
    FSMouse.midButton = []
    FSMouse.rightButton = []
    FSMouse.time = []
    gotValidClick = False  # until a click is received
    # store start times for FSinstructions
    FSinstructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    FSinstructions.tStart = globalClock.getTime(format='float')
    FSinstructions.status = STARTED
    thisExp.addData('FSinstructions.started', FSinstructions.tStart)
    FSinstructions.maxDuration = None
    # keep track of which components have finished
    FSinstructionsComponents = FSinstructions.components
    for thisComponent in FSinstructions.components:
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
    
    # --- Run Routine "FSinstructions" ---
    FSinstructions.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FSGenInsText* updates
        
        # if FSGenInsText is starting this frame...
        if FSGenInsText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FSGenInsText.frameNStart = frameN  # exact frame index
            FSGenInsText.tStart = t  # local t and not account for scr refresh
            FSGenInsText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FSGenInsText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'FSGenInsText.started')
            # update status
            FSGenInsText.status = STARTED
            FSGenInsText.setAutoDraw(True)
        
        # if FSGenInsText is active this frame...
        if FSGenInsText.status == STARTED:
            # update params
            pass
        # *FSMouse* updates
        
        # if FSMouse is starting this frame...
        if FSMouse.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            FSMouse.frameNStart = frameN  # exact frame index
            FSMouse.tStart = t  # local t and not account for scr refresh
            FSMouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FSMouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('FSMouse.started', t)
            # update status
            FSMouse.status = STARTED
            FSMouse.mouseClock.reset()
            prevButtonState = FSMouse.getPressed()  # if button is down already this ISN'T a new click
        if FSMouse.status == STARTED:  # only update if started and not finished!
            buttons = FSMouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    pass
                    x, y = FSMouse.getPos()
                    FSMouse.x.append(x)
                    FSMouse.y.append(y)
                    buttons = FSMouse.getPressed()
                    FSMouse.leftButton.append(buttons[0])
                    FSMouse.midButton.append(buttons[1])
                    FSMouse.rightButton.append(buttons[2])
                    FSMouse.time.append(FSMouse.mouseClock.getTime())
                    
                    continueRoutine = False  # end routine on response
        
        # *cont_buttonFSIns* updates
        
        # if cont_buttonFSIns is starting this frame...
        if cont_buttonFSIns.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            cont_buttonFSIns.frameNStart = frameN  # exact frame index
            cont_buttonFSIns.tStart = t  # local t and not account for scr refresh
            cont_buttonFSIns.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cont_buttonFSIns, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cont_buttonFSIns.started')
            # update status
            cont_buttonFSIns.status = STARTED
            cont_buttonFSIns.setAutoDraw(True)
        
        # if cont_buttonFSIns is active this frame...
        if cont_buttonFSIns.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            FSinstructions.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FSinstructions.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "FSinstructions" ---
    for thisComponent in FSinstructions.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for FSinstructions
    FSinstructions.tStop = globalClock.getTime(format='float')
    FSinstructions.tStopRefresh = tThisFlipGlobal
    thisExp.addData('FSinstructions.stopped', FSinstructions.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('FSMouse.x', FSMouse.x)
    thisExp.addData('FSMouse.y', FSMouse.y)
    thisExp.addData('FSMouse.leftButton', FSMouse.leftButton)
    thisExp.addData('FSMouse.midButton', FSMouse.midButton)
    thisExp.addData('FSMouse.rightButton', FSMouse.rightButton)
    thisExp.addData('FSMouse.time', FSMouse.time)
    thisExp.nextEntry()
    # the Routine "FSinstructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trialFSpractice = data.TrialHandler2(
        name='trialFSpractice',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('digitSpanPractice.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(trialFSpractice)  # add the loop to the experiment
    thisTrialFSpractice = trialFSpractice.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrialFSpractice.rgb)
    if thisTrialFSpractice != None:
        for paramName in thisTrialFSpractice:
            globals()[paramName] = thisTrialFSpractice[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrialFSpractice in trialFSpractice:
        currentLoop = trialFSpractice
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrialFSpractice.rgb)
        if thisTrialFSpractice != None:
            for paramName in thisTrialFSpractice:
                globals()[paramName] = thisTrialFSpractice[paramName]
        
        # set up handler to look after randomisation of conditions etc
        digitLoopPractice = data.TrialHandler2(
            name='digitLoopPractice',
            nReps=digitSpan, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(digitLoopPractice)  # add the loop to the experiment
        thisDigitLoopPractice = digitLoopPractice.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisDigitLoopPractice.rgb)
        if thisDigitLoopPractice != None:
            for paramName in thisDigitLoopPractice:
                globals()[paramName] = thisDigitLoopPractice[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisDigitLoopPractice in digitLoopPractice:
            currentLoop = digitLoopPractice
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisDigitLoopPractice.rgb)
            if thisDigitLoopPractice != None:
                for paramName in thisDigitLoopPractice:
                    globals()[paramName] = thisDigitLoopPractice[paramName]
            
            # --- Prepare to start Routine "showNumbersPractice" ---
            # create an object to store info about Routine showNumbersPractice
            showNumbersPractice = data.Routine(
                name='showNumbersPractice',
                components=[fixation_2, pres_text_practice],
            )
            showNumbersPractice.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            pres_text_practice.setText(str(digits)[digitLoopPractice.thisN])
            # store start times for showNumbersPractice
            showNumbersPractice.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            showNumbersPractice.tStart = globalClock.getTime(format='float')
            showNumbersPractice.status = STARTED
            thisExp.addData('showNumbersPractice.started', showNumbersPractice.tStart)
            showNumbersPractice.maxDuration = None
            # keep track of which components have finished
            showNumbersPracticeComponents = showNumbersPractice.components
            for thisComponent in showNumbersPractice.components:
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
            
            # --- Run Routine "showNumbersPractice" ---
            # if trial has changed, end Routine now
            if isinstance(digitLoopPractice, data.TrialHandler2) and thisDigitLoopPractice.thisN != digitLoopPractice.thisTrial.thisN:
                continueRoutine = False
            showNumbersPractice.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 2.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fixation_2* updates
                
                # if fixation_2 is starting this frame...
                if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixation_2.frameNStart = frameN  # exact frame index
                    fixation_2.tStart = t  # local t and not account for scr refresh
                    fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_2.started')
                    # update status
                    fixation_2.status = STARTED
                    fixation_2.setAutoDraw(True)
                
                # if fixation_2 is active this frame...
                if fixation_2.status == STARTED:
                    # update params
                    pass
                
                # if fixation_2 is stopping this frame...
                if fixation_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixation_2.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        fixation_2.tStop = t  # not accounting for scr refresh
                        fixation_2.tStopRefresh = tThisFlipGlobal  # on global time
                        fixation_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixation_2.stopped')
                        # update status
                        fixation_2.status = FINISHED
                        fixation_2.setAutoDraw(False)
                
                # *pres_text_practice* updates
                
                # if pres_text_practice is starting this frame...
                if pres_text_practice.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    pres_text_practice.frameNStart = frameN  # exact frame index
                    pres_text_practice.tStart = t  # local t and not account for scr refresh
                    pres_text_practice.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pres_text_practice, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'pres_text_practice.started')
                    # update status
                    pres_text_practice.status = STARTED
                    pres_text_practice.setAutoDraw(True)
                
                # if pres_text_practice is active this frame...
                if pres_text_practice.status == STARTED:
                    # update params
                    pass
                
                # if pres_text_practice is stopping this frame...
                if pres_text_practice.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > pres_text_practice.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        pres_text_practice.tStop = t  # not accounting for scr refresh
                        pres_text_practice.tStopRefresh = tThisFlipGlobal  # on global time
                        pres_text_practice.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'pres_text_practice.stopped')
                        # update status
                        pres_text_practice.status = FINISHED
                        pres_text_practice.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    showNumbersPractice.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in showNumbersPractice.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "showNumbersPractice" ---
            for thisComponent in showNumbersPractice.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for showNumbersPractice
            showNumbersPractice.tStop = globalClock.getTime(format='float')
            showNumbersPractice.tStopRefresh = tThisFlipGlobal
            thisExp.addData('showNumbersPractice.stopped', showNumbersPractice.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if showNumbersPractice.maxDurationReached:
                routineTimer.addTime(-showNumbersPractice.maxDuration)
            elif showNumbersPractice.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-2.000000)
            thisExp.nextEntry()
            
        # completed digitSpan repeats of 'digitLoopPractice'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "recallPractice" ---
        # create an object to store info about Routine recallPractice
        recallPractice = data.Routine(
            name='recallPractice',
            components=[recall_txtPractice, textboxPractice, cont_buttonPractice, mousePractice],
        )
        recallPractice.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        textboxPractice.reset()
        # setup some python lists for storing info about the mousePractice
        mousePractice.clicked_name = []
        gotValidClick = False  # until a click is received
        # store start times for recallPractice
        recallPractice.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        recallPractice.tStart = globalClock.getTime(format='float')
        recallPractice.status = STARTED
        thisExp.addData('recallPractice.started', recallPractice.tStart)
        recallPractice.maxDuration = None
        # keep track of which components have finished
        recallPracticeComponents = recallPractice.components
        for thisComponent in recallPractice.components:
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
        
        # --- Run Routine "recallPractice" ---
        # if trial has changed, end Routine now
        if isinstance(trialFSpractice, data.TrialHandler2) and thisTrialFSpractice.thisN != trialFSpractice.thisTrial.thisN:
            continueRoutine = False
        recallPractice.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *recall_txtPractice* updates
            
            # if recall_txtPractice is starting this frame...
            if recall_txtPractice.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                recall_txtPractice.frameNStart = frameN  # exact frame index
                recall_txtPractice.tStart = t  # local t and not account for scr refresh
                recall_txtPractice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(recall_txtPractice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'recall_txtPractice.started')
                # update status
                recall_txtPractice.status = STARTED
                recall_txtPractice.setAutoDraw(True)
            
            # if recall_txtPractice is active this frame...
            if recall_txtPractice.status == STARTED:
                # update params
                pass
            
            # *textboxPractice* updates
            
            # if textboxPractice is starting this frame...
            if textboxPractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textboxPractice.frameNStart = frameN  # exact frame index
                textboxPractice.tStart = t  # local t and not account for scr refresh
                textboxPractice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textboxPractice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textboxPractice.started')
                # update status
                textboxPractice.status = STARTED
                textboxPractice.setAutoDraw(True)
            
            # if textboxPractice is active this frame...
            if textboxPractice.status == STARTED:
                # update params
                pass
            
            # *cont_buttonPractice* updates
            
            # if cont_buttonPractice is starting this frame...
            if cont_buttonPractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cont_buttonPractice.frameNStart = frameN  # exact frame index
                cont_buttonPractice.tStart = t  # local t and not account for scr refresh
                cont_buttonPractice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cont_buttonPractice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cont_buttonPractice.started')
                # update status
                cont_buttonPractice.status = STARTED
                cont_buttonPractice.setAutoDraw(True)
            
            # if cont_buttonPractice is active this frame...
            if cont_buttonPractice.status == STARTED:
                # update params
                pass
            # *mousePractice* updates
            
            # if mousePractice is starting this frame...
            if mousePractice.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mousePractice.frameNStart = frameN  # exact frame index
                mousePractice.tStart = t  # local t and not account for scr refresh
                mousePractice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mousePractice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mousePractice.started', t)
                # update status
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
                        clickableList = environmenttools.getFromNames(cont_button, namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mousePractice):
                                gotValidClick = True
                                mousePractice.clicked_name.append(obj.name)
                        if not gotValidClick:
                            mousePractice.clicked_name.append(None)
                        if gotValidClick:  
                            continueRoutine = False  # end routine on response
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                recallPractice.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in recallPractice.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "recallPractice" ---
        for thisComponent in recallPractice.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for recallPractice
        recallPractice.tStop = globalClock.getTime(format='float')
        recallPractice.tStopRefresh = tThisFlipGlobal
        thisExp.addData('recallPractice.stopped', recallPractice.tStop)
        trialFSpractice.addData('textboxPractice.text',textboxPractice.text)
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
        # store data for trialFSpractice (TrialHandler)
        x, y = mousePractice.getPos()
        buttons = mousePractice.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            clickableList = environmenttools.getFromNames(cont_button, namespace=locals())
            for obj in clickableList:
                # is this object clicked on?
                if obj.contains(mousePractice):
                    gotValidClick = True
                    mousePractice.clicked_name.append(obj.name)
            if not gotValidClick:
                mousePractice.clicked_name.append(None)
        trialFSpractice.addData('mousePractice.x', x)
        trialFSpractice.addData('mousePractice.y', y)
        trialFSpractice.addData('mousePractice.leftButton', buttons[0])
        trialFSpractice.addData('mousePractice.midButton', buttons[1])
        trialFSpractice.addData('mousePractice.rightButton', buttons[2])
        if len(mousePractice.clicked_name):
            trialFSpractice.addData('mousePractice.clicked_name', mousePractice.clicked_name[0])
        # the Routine "recallPractice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedbackPractice" ---
        # create an object to store info about Routine feedbackPractice
        feedbackPractice = data.Routine(
            name='feedbackPractice',
            components=[feedbac_textPractice],
        )
        feedbackPractice.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        feedbac_textPractice.setText(fbTxt)
        # store start times for feedbackPractice
        feedbackPractice.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        feedbackPractice.tStart = globalClock.getTime(format='float')
        feedbackPractice.status = STARTED
        thisExp.addData('feedbackPractice.started', feedbackPractice.tStart)
        feedbackPractice.maxDuration = None
        # keep track of which components have finished
        feedbackPracticeComponents = feedbackPractice.components
        for thisComponent in feedbackPractice.components:
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
        
        # --- Run Routine "feedbackPractice" ---
        # if trial has changed, end Routine now
        if isinstance(trialFSpractice, data.TrialHandler2) and thisTrialFSpractice.thisN != trialFSpractice.thisTrial.thisN:
            continueRoutine = False
        feedbackPractice.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedbac_textPractice* updates
            
            # if feedbac_textPractice is starting this frame...
            if feedbac_textPractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedbac_textPractice.frameNStart = frameN  # exact frame index
                feedbac_textPractice.tStart = t  # local t and not account for scr refresh
                feedbac_textPractice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedbac_textPractice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedbac_textPractice.started')
                # update status
                feedbac_textPractice.status = STARTED
                feedbac_textPractice.setAutoDraw(True)
            
            # if feedbac_textPractice is active this frame...
            if feedbac_textPractice.status == STARTED:
                # update params
                pass
            
            # if feedbac_textPractice is stopping this frame...
            if feedbac_textPractice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedbac_textPractice.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    feedbac_textPractice.tStop = t  # not accounting for scr refresh
                    feedbac_textPractice.tStopRefresh = tThisFlipGlobal  # on global time
                    feedbac_textPractice.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedbac_textPractice.stopped')
                    # update status
                    feedbac_textPractice.status = FINISHED
                    feedbac_textPractice.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                feedbackPractice.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackPractice.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedbackPractice" ---
        for thisComponent in feedbackPractice.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for feedbackPractice
        feedbackPractice.tStop = globalClock.getTime(format='float')
        feedbackPractice.tStopRefresh = tThisFlipGlobal
        thisExp.addData('feedbackPractice.stopped', feedbackPractice.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if feedbackPractice.maxDurationReached:
            routineTimer.addTime(-feedbackPractice.maxDuration)
        elif feedbackPractice.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trialFSpractice'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "startRealFS" ---
    # create an object to store info about Routine startRealFS
    startRealFS = data.Routine(
        name='startRealFS',
        components=[text],
    )
    startRealFS.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for startRealFS
    startRealFS.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    startRealFS.tStart = globalClock.getTime(format='float')
    startRealFS.status = STARTED
    thisExp.addData('startRealFS.started', startRealFS.tStart)
    startRealFS.maxDuration = None
    # keep track of which components have finished
    startRealFSComponents = startRealFS.components
    for thisComponent in startRealFS.components:
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
    
    # --- Run Routine "startRealFS" ---
    startRealFS.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # if text is stopping this frame...
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.tStopRefresh = tThisFlipGlobal  # on global time
                text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.stopped')
                # update status
                text.status = FINISHED
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            startRealFS.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in startRealFS.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "startRealFS" ---
    for thisComponent in startRealFS.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for startRealFS
    startRealFS.tStop = globalClock.getTime(format='float')
    startRealFS.tStopRefresh = tThisFlipGlobal
    thisExp.addData('startRealFS.stopped', startRealFS.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if startRealFS.maxDurationReached:
        routineTimer.addTime(-startRealFS.maxDuration)
    elif startRealFS.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler2(
        name='trials',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions(
        'digitSpanTrialNumber.xlsx', 
        selection='0:1'
    )
    , 
        seed=None, 
    )
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "selectNumbers" ---
        # create an object to store info about Routine selectNumbers
        selectNumbers = data.Routine(
            name='selectNumbers',
            components=[],
        )
        selectNumbers.status = NOT_STARTED
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
        # store start times for selectNumbers
        selectNumbers.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        selectNumbers.tStart = globalClock.getTime(format='float')
        selectNumbers.status = STARTED
        thisExp.addData('selectNumbers.started', selectNumbers.tStart)
        selectNumbers.maxDuration = None
        # keep track of which components have finished
        selectNumbersComponents = selectNumbers.components
        for thisComponent in selectNumbers.components:
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
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        selectNumbers.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                selectNumbers.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in selectNumbers.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "selectNumbers" ---
        for thisComponent in selectNumbers.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for selectNumbers
        selectNumbers.tStop = globalClock.getTime(format='float')
        selectNumbers.tStopRefresh = tThisFlipGlobal
        thisExp.addData('selectNumbers.stopped', selectNumbers.tStop)
        # the Routine "selectNumbers" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        digitLoop = data.TrialHandler2(
            name='digitLoop',
            nReps=digitSpan, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(digitLoop)  # add the loop to the experiment
        thisDigitLoop = digitLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisDigitLoop.rgb)
        if thisDigitLoop != None:
            for paramName in thisDigitLoop:
                globals()[paramName] = thisDigitLoop[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisDigitLoop in digitLoop:
            currentLoop = digitLoop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisDigitLoop.rgb)
            if thisDigitLoop != None:
                for paramName in thisDigitLoop:
                    globals()[paramName] = thisDigitLoop[paramName]
            
            # --- Prepare to start Routine "showNumbers" ---
            # create an object to store info about Routine showNumbers
            showNumbers = data.Routine(
                name='showNumbers',
                components=[fixation, presentation_text],
            )
            showNumbers.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from getTmpNumberCodeFS
            tmpNumber = digitsForTrial[digitLoop.thisN]
            presentation_text.setText(tmpNumber)
            # store start times for showNumbers
            showNumbers.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            showNumbers.tStart = globalClock.getTime(format='float')
            showNumbers.status = STARTED
            thisExp.addData('showNumbers.started', showNumbers.tStart)
            showNumbers.maxDuration = None
            # keep track of which components have finished
            showNumbersComponents = showNumbers.components
            for thisComponent in showNumbers.components:
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
            
            # --- Run Routine "showNumbers" ---
            # if trial has changed, end Routine now
            if isinstance(digitLoop, data.TrialHandler2) and thisDigitLoop.thisN != digitLoop.thisTrial.thisN:
                continueRoutine = False
            showNumbers.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 2.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fixation* updates
                
                # if fixation is starting this frame...
                if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixation.frameNStart = frameN  # exact frame index
                    fixation.tStart = t  # local t and not account for scr refresh
                    fixation.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation.started')
                    # update status
                    fixation.status = STARTED
                    fixation.setAutoDraw(True)
                
                # if fixation is active this frame...
                if fixation.status == STARTED:
                    # update params
                    pass
                
                # if fixation is stopping this frame...
                if fixation.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixation.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        fixation.tStop = t  # not accounting for scr refresh
                        fixation.tStopRefresh = tThisFlipGlobal  # on global time
                        fixation.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixation.stopped')
                        # update status
                        fixation.status = FINISHED
                        fixation.setAutoDraw(False)
                
                # *presentation_text* updates
                
                # if presentation_text is starting this frame...
                if presentation_text.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    presentation_text.frameNStart = frameN  # exact frame index
                    presentation_text.tStart = t  # local t and not account for scr refresh
                    presentation_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(presentation_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'presentation_text.started')
                    # update status
                    presentation_text.status = STARTED
                    presentation_text.setAutoDraw(True)
                
                # if presentation_text is active this frame...
                if presentation_text.status == STARTED:
                    # update params
                    pass
                
                # if presentation_text is stopping this frame...
                if presentation_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > presentation_text.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        presentation_text.tStop = t  # not accounting for scr refresh
                        presentation_text.tStopRefresh = tThisFlipGlobal  # on global time
                        presentation_text.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'presentation_text.stopped')
                        # update status
                        presentation_text.status = FINISHED
                        presentation_text.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    showNumbers.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in showNumbers.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "showNumbers" ---
            for thisComponent in showNumbers.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for showNumbers
            showNumbers.tStop = globalClock.getTime(format='float')
            showNumbers.tStopRefresh = tThisFlipGlobal
            thisExp.addData('showNumbers.stopped', showNumbers.tStop)
            # Run 'End Routine' code from getTmpNumberCodeFS
            thisExp.addData("digitsForTrial",digitsForTrial)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if showNumbers.maxDurationReached:
                routineTimer.addTime(-showNumbers.maxDuration)
            elif showNumbers.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-2.000000)
            thisExp.nextEntry()
            
        # completed digitSpan repeats of 'digitLoop'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "Recall" ---
        # create an object to store info about Routine Recall
        Recall = data.Routine(
            name='Recall',
            components=[recall_txt, textbox, cont_button, mouse],
        )
        Recall.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        textbox.reset()
        # setup some python lists for storing info about the mouse
        mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # store start times for Recall
        Recall.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Recall.tStart = globalClock.getTime(format='float')
        Recall.status = STARTED
        thisExp.addData('Recall.started', Recall.tStart)
        Recall.maxDuration = None
        # keep track of which components have finished
        RecallComponents = Recall.components
        for thisComponent in Recall.components:
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
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        Recall.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *recall_txt* updates
            
            # if recall_txt is starting this frame...
            if recall_txt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                recall_txt.frameNStart = frameN  # exact frame index
                recall_txt.tStart = t  # local t and not account for scr refresh
                recall_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(recall_txt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'recall_txt.started')
                # update status
                recall_txt.status = STARTED
                recall_txt.setAutoDraw(True)
            
            # if recall_txt is active this frame...
            if recall_txt.status == STARTED:
                # update params
                pass
            
            # *textbox* updates
            
            # if textbox is starting this frame...
            if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textbox.frameNStart = frameN  # exact frame index
                textbox.tStart = t  # local t and not account for scr refresh
                textbox.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox.started')
                # update status
                textbox.status = STARTED
                textbox.setAutoDraw(True)
            
            # if textbox is active this frame...
            if textbox.status == STARTED:
                # update params
                pass
            
            # *cont_button* updates
            
            # if cont_button is starting this frame...
            if cont_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cont_button.frameNStart = frameN  # exact frame index
                cont_button.tStart = t  # local t and not account for scr refresh
                cont_button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cont_button, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cont_button.started')
                # update status
                cont_button.status = STARTED
                cont_button.setAutoDraw(True)
            
            # if cont_button is active this frame...
            if cont_button.status == STARTED:
                # update params
                pass
            # *mouse* updates
            
            # if mouse is starting this frame...
            if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse.started', t)
                # update status
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames(cont_button, namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouse):
                                gotValidClick = True
                                mouse.clicked_name.append(obj.name)
                        if not gotValidClick:
                            mouse.clicked_name.append(None)
                        if gotValidClick:  
                            continueRoutine = False  # end routine on response
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Recall.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Recall.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Recall" ---
        for thisComponent in Recall.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Recall
        Recall.tStop = globalClock.getTime(format='float')
        Recall.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Recall.stopped', Recall.tStop)
        trials.addData('textbox.text',textbox.text)
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
        # store data for trials (TrialHandler)
        x, y = mouse.getPos()
        buttons = mouse.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            clickableList = environmenttools.getFromNames(cont_button, namespace=locals())
            for obj in clickableList:
                # is this object clicked on?
                if obj.contains(mouse):
                    gotValidClick = True
                    mouse.clicked_name.append(obj.name)
            if not gotValidClick:
                mouse.clicked_name.append(None)
        trials.addData('mouse.x', x)
        trials.addData('mouse.y', y)
        trials.addData('mouse.leftButton', buttons[0])
        trials.addData('mouse.midButton', buttons[1])
        trials.addData('mouse.rightButton', buttons[2])
        if len(mouse.clicked_name):
            trials.addData('mouse.clicked_name', mouse.clicked_name[0])
        # the Routine "Recall" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Feedback" ---
        # create an object to store info about Routine Feedback
        Feedback = data.Routine(
            name='Feedback',
            components=[feedback_text],
        )
        Feedback.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        feedback_text.setText(fbTxt)
        # store start times for Feedback
        Feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Feedback.tStart = globalClock.getTime(format='float')
        Feedback.status = STARTED
        thisExp.addData('Feedback.started', Feedback.tStart)
        Feedback.maxDuration = None
        # keep track of which components have finished
        FeedbackComponents = Feedback.components
        for thisComponent in Feedback.components:
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
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        Feedback.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_text* updates
            
            # if feedback_text is starting this frame...
            if feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_text.frameNStart = frameN  # exact frame index
                feedback_text.tStart = t  # local t and not account for scr refresh
                feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_text.started')
                # update status
                feedback_text.status = STARTED
                feedback_text.setAutoDraw(True)
            
            # if feedback_text is active this frame...
            if feedback_text.status == STARTED:
                # update params
                pass
            
            # if feedback_text is stopping this frame...
            if feedback_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_text.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_text.tStop = t  # not accounting for scr refresh
                    feedback_text.tStopRefresh = tThisFlipGlobal  # on global time
                    feedback_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_text.stopped')
                    # update status
                    feedback_text.status = FINISHED
                    feedback_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Feedback.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Feedback.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Feedback" ---
        for thisComponent in Feedback.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Feedback
        Feedback.tStop = globalClock.getTime(format='float')
        Feedback.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Feedback.stopped', Feedback.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Feedback.maxDurationReached:
            routineTimer.addTime(-Feedback.maxDuration)
        elif Feedback.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "instructionsBS" ---
    # create an object to store info about Routine instructionsBS
    instructionsBS = data.Routine(
        name='instructionsBS',
        components=[BSGenInsText, BSMouse, cont_buttonBSIns],
    )
    instructionsBS.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the BSMouse
    BSMouse.x = []
    BSMouse.y = []
    BSMouse.leftButton = []
    BSMouse.midButton = []
    BSMouse.rightButton = []
    BSMouse.time = []
    gotValidClick = False  # until a click is received
    # store start times for instructionsBS
    instructionsBS.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instructionsBS.tStart = globalClock.getTime(format='float')
    instructionsBS.status = STARTED
    thisExp.addData('instructionsBS.started', instructionsBS.tStart)
    instructionsBS.maxDuration = None
    # keep track of which components have finished
    instructionsBSComponents = instructionsBS.components
    for thisComponent in instructionsBS.components:
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
    
    # --- Run Routine "instructionsBS" ---
    instructionsBS.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *BSGenInsText* updates
        
        # if BSGenInsText is starting this frame...
        if BSGenInsText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            BSGenInsText.frameNStart = frameN  # exact frame index
            BSGenInsText.tStart = t  # local t and not account for scr refresh
            BSGenInsText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BSGenInsText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'BSGenInsText.started')
            # update status
            BSGenInsText.status = STARTED
            BSGenInsText.setAutoDraw(True)
        
        # if BSGenInsText is active this frame...
        if BSGenInsText.status == STARTED:
            # update params
            pass
        # *BSMouse* updates
        
        # if BSMouse is starting this frame...
        if BSMouse.status == NOT_STARTED and t >= 5-frameTolerance:
            # keep track of start time/frame for later
            BSMouse.frameNStart = frameN  # exact frame index
            BSMouse.tStart = t  # local t and not account for scr refresh
            BSMouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BSMouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('BSMouse.started', t)
            # update status
            BSMouse.status = STARTED
            BSMouse.mouseClock.reset()
            prevButtonState = BSMouse.getPressed()  # if button is down already this ISN'T a new click
        if BSMouse.status == STARTED:  # only update if started and not finished!
            buttons = BSMouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    pass
                    x, y = BSMouse.getPos()
                    BSMouse.x.append(x)
                    BSMouse.y.append(y)
                    buttons = BSMouse.getPressed()
                    BSMouse.leftButton.append(buttons[0])
                    BSMouse.midButton.append(buttons[1])
                    BSMouse.rightButton.append(buttons[2])
                    BSMouse.time.append(BSMouse.mouseClock.getTime())
                    
                    continueRoutine = False  # end routine on response
        
        # *cont_buttonBSIns* updates
        
        # if cont_buttonBSIns is starting this frame...
        if cont_buttonBSIns.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            cont_buttonBSIns.frameNStart = frameN  # exact frame index
            cont_buttonBSIns.tStart = t  # local t and not account for scr refresh
            cont_buttonBSIns.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cont_buttonBSIns, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cont_buttonBSIns.started')
            # update status
            cont_buttonBSIns.status = STARTED
            cont_buttonBSIns.setAutoDraw(True)
        
        # if cont_buttonBSIns is active this frame...
        if cont_buttonBSIns.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instructionsBS.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsBS.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructionsBS" ---
    for thisComponent in instructionsBS.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instructionsBS
    instructionsBS.tStop = globalClock.getTime(format='float')
    instructionsBS.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instructionsBS.stopped', instructionsBS.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('BSMouse.x', BSMouse.x)
    thisExp.addData('BSMouse.y', BSMouse.y)
    thisExp.addData('BSMouse.leftButton', BSMouse.leftButton)
    thisExp.addData('BSMouse.midButton', BSMouse.midButton)
    thisExp.addData('BSMouse.rightButton', BSMouse.rightButton)
    thisExp.addData('BSMouse.time', BSMouse.time)
    thisExp.nextEntry()
    # the Routine "instructionsBS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trialsPracticeBS = data.TrialHandler2(
        name='trialsPracticeBS',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('digitSpanPractice.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(trialsPracticeBS)  # add the loop to the experiment
    thisTrialsPracticeBS = trialsPracticeBS.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsPracticeBS.rgb)
    if thisTrialsPracticeBS != None:
        for paramName in thisTrialsPracticeBS:
            globals()[paramName] = thisTrialsPracticeBS[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrialsPracticeBS in trialsPracticeBS:
        currentLoop = trialsPracticeBS
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrialsPracticeBS.rgb)
        if thisTrialsPracticeBS != None:
            for paramName in thisTrialsPracticeBS:
                globals()[paramName] = thisTrialsPracticeBS[paramName]
        
        # set up handler to look after randomisation of conditions etc
        digitLoopPracticeBS = data.TrialHandler2(
            name='digitLoopPracticeBS',
            nReps=digitSpan, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(digitLoopPracticeBS)  # add the loop to the experiment
        thisDigitLoopPracticeBS = digitLoopPracticeBS.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisDigitLoopPracticeBS.rgb)
        if thisDigitLoopPracticeBS != None:
            for paramName in thisDigitLoopPracticeBS:
                globals()[paramName] = thisDigitLoopPracticeBS[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisDigitLoopPracticeBS in digitLoopPracticeBS:
            currentLoop = digitLoopPracticeBS
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisDigitLoopPracticeBS.rgb)
            if thisDigitLoopPracticeBS != None:
                for paramName in thisDigitLoopPracticeBS:
                    globals()[paramName] = thisDigitLoopPracticeBS[paramName]
            
            # --- Prepare to start Routine "showNumbersPracticeBS_2" ---
            # create an object to store info about Routine showNumbersPracticeBS_2
            showNumbersPracticeBS_2 = data.Routine(
                name='showNumbersPracticeBS_2',
                components=[fixation_3, pres_text_practice_2],
            )
            showNumbersPracticeBS_2.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            pres_text_practice_2.setText(str(digits)[digitLoopPracticeBS.thisN])
            # store start times for showNumbersPracticeBS_2
            showNumbersPracticeBS_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            showNumbersPracticeBS_2.tStart = globalClock.getTime(format='float')
            showNumbersPracticeBS_2.status = STARTED
            thisExp.addData('showNumbersPracticeBS_2.started', showNumbersPracticeBS_2.tStart)
            showNumbersPracticeBS_2.maxDuration = None
            # keep track of which components have finished
            showNumbersPracticeBS_2Components = showNumbersPracticeBS_2.components
            for thisComponent in showNumbersPracticeBS_2.components:
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
            
            # --- Run Routine "showNumbersPracticeBS_2" ---
            # if trial has changed, end Routine now
            if isinstance(digitLoopPracticeBS, data.TrialHandler2) and thisDigitLoopPracticeBS.thisN != digitLoopPracticeBS.thisTrial.thisN:
                continueRoutine = False
            showNumbersPracticeBS_2.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 2.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fixation_3* updates
                
                # if fixation_3 is starting this frame...
                if fixation_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixation_3.frameNStart = frameN  # exact frame index
                    fixation_3.tStart = t  # local t and not account for scr refresh
                    fixation_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_3.started')
                    # update status
                    fixation_3.status = STARTED
                    fixation_3.setAutoDraw(True)
                
                # if fixation_3 is active this frame...
                if fixation_3.status == STARTED:
                    # update params
                    pass
                
                # if fixation_3 is stopping this frame...
                if fixation_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixation_3.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        fixation_3.tStop = t  # not accounting for scr refresh
                        fixation_3.tStopRefresh = tThisFlipGlobal  # on global time
                        fixation_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixation_3.stopped')
                        # update status
                        fixation_3.status = FINISHED
                        fixation_3.setAutoDraw(False)
                
                # *pres_text_practice_2* updates
                
                # if pres_text_practice_2 is starting this frame...
                if pres_text_practice_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    pres_text_practice_2.frameNStart = frameN  # exact frame index
                    pres_text_practice_2.tStart = t  # local t and not account for scr refresh
                    pres_text_practice_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pres_text_practice_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'pres_text_practice_2.started')
                    # update status
                    pres_text_practice_2.status = STARTED
                    pres_text_practice_2.setAutoDraw(True)
                
                # if pres_text_practice_2 is active this frame...
                if pres_text_practice_2.status == STARTED:
                    # update params
                    pass
                
                # if pres_text_practice_2 is stopping this frame...
                if pres_text_practice_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > pres_text_practice_2.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        pres_text_practice_2.tStop = t  # not accounting for scr refresh
                        pres_text_practice_2.tStopRefresh = tThisFlipGlobal  # on global time
                        pres_text_practice_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'pres_text_practice_2.stopped')
                        # update status
                        pres_text_practice_2.status = FINISHED
                        pres_text_practice_2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    showNumbersPracticeBS_2.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in showNumbersPracticeBS_2.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "showNumbersPracticeBS_2" ---
            for thisComponent in showNumbersPracticeBS_2.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for showNumbersPracticeBS_2
            showNumbersPracticeBS_2.tStop = globalClock.getTime(format='float')
            showNumbersPracticeBS_2.tStopRefresh = tThisFlipGlobal
            thisExp.addData('showNumbersPracticeBS_2.stopped', showNumbersPracticeBS_2.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if showNumbersPracticeBS_2.maxDurationReached:
                routineTimer.addTime(-showNumbersPracticeBS_2.maxDuration)
            elif showNumbersPracticeBS_2.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-2.000000)
            thisExp.nextEntry()
            
        # completed digitSpan repeats of 'digitLoopPracticeBS'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "recallPracticeBS" ---
        # create an object to store info about Routine recallPracticeBS
        recallPracticeBS = data.Routine(
            name='recallPracticeBS',
            components=[recall_txtPractice_2, textboxPractice_2, cont_buttonPractice_2, mousePractice_2],
        )
        recallPracticeBS.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        textboxPractice_2.reset()
        # setup some python lists for storing info about the mousePractice_2
        mousePractice_2.clicked_name = []
        gotValidClick = False  # until a click is received
        # store start times for recallPracticeBS
        recallPracticeBS.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        recallPracticeBS.tStart = globalClock.getTime(format='float')
        recallPracticeBS.status = STARTED
        thisExp.addData('recallPracticeBS.started', recallPracticeBS.tStart)
        recallPracticeBS.maxDuration = None
        # keep track of which components have finished
        recallPracticeBSComponents = recallPracticeBS.components
        for thisComponent in recallPracticeBS.components:
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
        # if trial has changed, end Routine now
        if isinstance(trialsPracticeBS, data.TrialHandler2) and thisTrialsPracticeBS.thisN != trialsPracticeBS.thisTrial.thisN:
            continueRoutine = False
        recallPracticeBS.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *recall_txtPractice_2* updates
            
            # if recall_txtPractice_2 is starting this frame...
            if recall_txtPractice_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                recall_txtPractice_2.frameNStart = frameN  # exact frame index
                recall_txtPractice_2.tStart = t  # local t and not account for scr refresh
                recall_txtPractice_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(recall_txtPractice_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'recall_txtPractice_2.started')
                # update status
                recall_txtPractice_2.status = STARTED
                recall_txtPractice_2.setAutoDraw(True)
            
            # if recall_txtPractice_2 is active this frame...
            if recall_txtPractice_2.status == STARTED:
                # update params
                pass
            
            # *textboxPractice_2* updates
            
            # if textboxPractice_2 is starting this frame...
            if textboxPractice_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textboxPractice_2.frameNStart = frameN  # exact frame index
                textboxPractice_2.tStart = t  # local t and not account for scr refresh
                textboxPractice_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textboxPractice_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textboxPractice_2.started')
                # update status
                textboxPractice_2.status = STARTED
                textboxPractice_2.setAutoDraw(True)
            
            # if textboxPractice_2 is active this frame...
            if textboxPractice_2.status == STARTED:
                # update params
                pass
            
            # *cont_buttonPractice_2* updates
            
            # if cont_buttonPractice_2 is starting this frame...
            if cont_buttonPractice_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cont_buttonPractice_2.frameNStart = frameN  # exact frame index
                cont_buttonPractice_2.tStart = t  # local t and not account for scr refresh
                cont_buttonPractice_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cont_buttonPractice_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cont_buttonPractice_2.started')
                # update status
                cont_buttonPractice_2.status = STARTED
                cont_buttonPractice_2.setAutoDraw(True)
            
            # if cont_buttonPractice_2 is active this frame...
            if cont_buttonPractice_2.status == STARTED:
                # update params
                pass
            # *mousePractice_2* updates
            
            # if mousePractice_2 is starting this frame...
            if mousePractice_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mousePractice_2.frameNStart = frameN  # exact frame index
                mousePractice_2.tStart = t  # local t and not account for scr refresh
                mousePractice_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mousePractice_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mousePractice_2.started', t)
                # update status
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
                        clickableList = environmenttools.getFromNames(cont_button, namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mousePractice_2):
                                gotValidClick = True
                                mousePractice_2.clicked_name.append(obj.name)
                        if not gotValidClick:
                            mousePractice_2.clicked_name.append(None)
                        if gotValidClick:  
                            continueRoutine = False  # end routine on response
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                recallPracticeBS.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in recallPracticeBS.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "recallPracticeBS" ---
        for thisComponent in recallPracticeBS.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for recallPracticeBS
        recallPracticeBS.tStop = globalClock.getTime(format='float')
        recallPracticeBS.tStopRefresh = tThisFlipGlobal
        thisExp.addData('recallPracticeBS.stopped', recallPracticeBS.tStop)
        trialsPracticeBS.addData('textboxPractice_2.text',textboxPractice_2.text)
        # Run 'End Routine' code from code_3practice_2
        #for r in range(len(digitsForTrial)):
        #    digitsForTrial[r] = str(digitsForTrial[r])
        
        #digitsForTrial = ''.join(digitsForTrial)
        
        
        if textboxPractice_2.text == str(digitsReverse):
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
            clickableList = environmenttools.getFromNames(cont_button, namespace=locals())
            for obj in clickableList:
                # is this object clicked on?
                if obj.contains(mousePractice_2):
                    gotValidClick = True
                    mousePractice_2.clicked_name.append(obj.name)
            if not gotValidClick:
                mousePractice_2.clicked_name.append(None)
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
        # create an object to store info about Routine feedbackPracticeBS
        feedbackPracticeBS = data.Routine(
            name='feedbackPracticeBS',
            components=[feedbac_textPractice_2],
        )
        feedbackPracticeBS.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        feedbac_textPractice_2.setText(fbTxt)
        # store start times for feedbackPracticeBS
        feedbackPracticeBS.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        feedbackPracticeBS.tStart = globalClock.getTime(format='float')
        feedbackPracticeBS.status = STARTED
        thisExp.addData('feedbackPracticeBS.started', feedbackPracticeBS.tStart)
        feedbackPracticeBS.maxDuration = None
        # keep track of which components have finished
        feedbackPracticeBSComponents = feedbackPracticeBS.components
        for thisComponent in feedbackPracticeBS.components:
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
        # if trial has changed, end Routine now
        if isinstance(trialsPracticeBS, data.TrialHandler2) and thisTrialsPracticeBS.thisN != trialsPracticeBS.thisTrial.thisN:
            continueRoutine = False
        feedbackPracticeBS.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedbac_textPractice_2* updates
            
            # if feedbac_textPractice_2 is starting this frame...
            if feedbac_textPractice_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedbac_textPractice_2.frameNStart = frameN  # exact frame index
                feedbac_textPractice_2.tStart = t  # local t and not account for scr refresh
                feedbac_textPractice_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedbac_textPractice_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedbac_textPractice_2.started')
                # update status
                feedbac_textPractice_2.status = STARTED
                feedbac_textPractice_2.setAutoDraw(True)
            
            # if feedbac_textPractice_2 is active this frame...
            if feedbac_textPractice_2.status == STARTED:
                # update params
                pass
            
            # if feedbac_textPractice_2 is stopping this frame...
            if feedbac_textPractice_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedbac_textPractice_2.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    feedbac_textPractice_2.tStop = t  # not accounting for scr refresh
                    feedbac_textPractice_2.tStopRefresh = tThisFlipGlobal  # on global time
                    feedbac_textPractice_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedbac_textPractice_2.stopped')
                    # update status
                    feedbac_textPractice_2.status = FINISHED
                    feedbac_textPractice_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                feedbackPracticeBS.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackPracticeBS.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedbackPracticeBS" ---
        for thisComponent in feedbackPracticeBS.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for feedbackPracticeBS
        feedbackPracticeBS.tStop = globalClock.getTime(format='float')
        feedbackPracticeBS.tStopRefresh = tThisFlipGlobal
        thisExp.addData('feedbackPracticeBS.stopped', feedbackPracticeBS.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if feedbackPracticeBS.maxDurationReached:
            routineTimer.addTime(-feedbackPracticeBS.maxDuration)
        elif feedbackPracticeBS.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trialsPracticeBS'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "startRealBS" ---
    # create an object to store info about Routine startRealBS
    startRealBS = data.Routine(
        name='startRealBS',
        components=[text_2],
    )
    startRealBS.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for startRealBS
    startRealBS.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    startRealBS.tStart = globalClock.getTime(format='float')
    startRealBS.status = STARTED
    thisExp.addData('startRealBS.started', startRealBS.tStart)
    startRealBS.maxDuration = None
    # keep track of which components have finished
    startRealBSComponents = startRealBS.components
    for thisComponent in startRealBS.components:
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
    startRealBS.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        
        # if text_2 is starting this frame...
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.started')
            # update status
            text_2.status = STARTED
            text_2.setAutoDraw(True)
        
        # if text_2 is active this frame...
        if text_2.status == STARTED:
            # update params
            pass
        
        # if text_2 is stopping this frame...
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.tStopRefresh = tThisFlipGlobal  # on global time
                text_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.stopped')
                # update status
                text_2.status = FINISHED
                text_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            startRealBS.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in startRealBS.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "startRealBS" ---
    for thisComponent in startRealBS.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for startRealBS
    startRealBS.tStop = globalClock.getTime(format='float')
    startRealBS.tStopRefresh = tThisFlipGlobal
    thisExp.addData('startRealBS.stopped', startRealBS.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if startRealBS.maxDurationReached:
        routineTimer.addTime(-startRealBS.maxDuration)
    elif startRealBS.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    trialsBS = data.TrialHandler2(
        name='trialsBS',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions(
        'digitSpanTrialNumber.xlsx', 
        selection='0:1'
    )
    , 
        seed=None, 
    )
    thisExp.addLoop(trialsBS)  # add the loop to the experiment
    thisTrialsBS = trialsBS.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsBS.rgb)
    if thisTrialsBS != None:
        for paramName in thisTrialsBS:
            globals()[paramName] = thisTrialsBS[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrialsBS in trialsBS:
        currentLoop = trialsBS
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrialsBS.rgb)
        if thisTrialsBS != None:
            for paramName in thisTrialsBS:
                globals()[paramName] = thisTrialsBS[paramName]
        
        # --- Prepare to start Routine "selectNumbersBS" ---
        # create an object to store info about Routine selectNumbersBS
        selectNumbersBS = data.Routine(
            name='selectNumbersBS',
            components=[],
        )
        selectNumbersBS.status = NOT_STARTED
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
        # store start times for selectNumbersBS
        selectNumbersBS.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        selectNumbersBS.tStart = globalClock.getTime(format='float')
        selectNumbersBS.status = STARTED
        thisExp.addData('selectNumbersBS.started', selectNumbersBS.tStart)
        selectNumbersBS.maxDuration = None
        # keep track of which components have finished
        selectNumbersBSComponents = selectNumbersBS.components
        for thisComponent in selectNumbersBS.components:
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
        # if trial has changed, end Routine now
        if isinstance(trialsBS, data.TrialHandler2) and thisTrialsBS.thisN != trialsBS.thisTrial.thisN:
            continueRoutine = False
        selectNumbersBS.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                selectNumbersBS.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in selectNumbersBS.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "selectNumbersBS" ---
        for thisComponent in selectNumbersBS.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for selectNumbersBS
        selectNumbersBS.tStop = globalClock.getTime(format='float')
        selectNumbersBS.tStopRefresh = tThisFlipGlobal
        thisExp.addData('selectNumbersBS.stopped', selectNumbersBS.tStop)
        # the Routine "selectNumbersBS" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        digitLoopBS = data.TrialHandler2(
            name='digitLoopBS',
            nReps=digitSpan, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(digitLoopBS)  # add the loop to the experiment
        thisDigitLoopBS = digitLoopBS.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisDigitLoopBS.rgb)
        if thisDigitLoopBS != None:
            for paramName in thisDigitLoopBS:
                globals()[paramName] = thisDigitLoopBS[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisDigitLoopBS in digitLoopBS:
            currentLoop = digitLoopBS
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisDigitLoopBS.rgb)
            if thisDigitLoopBS != None:
                for paramName in thisDigitLoopBS:
                    globals()[paramName] = thisDigitLoopBS[paramName]
            
            # --- Prepare to start Routine "showNumbersBS" ---
            # create an object to store info about Routine showNumbersBS
            showNumbersBS = data.Routine(
                name='showNumbersBS',
                components=[fixationBS, presentation_textBS],
            )
            showNumbersBS.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from getTmpNumberCodeBS
            tmpNumber = digitsForTrial[digitLoopBS.thisN]
            presentation_textBS.setText(tmpNumber)
            # store start times for showNumbersBS
            showNumbersBS.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            showNumbersBS.tStart = globalClock.getTime(format='float')
            showNumbersBS.status = STARTED
            thisExp.addData('showNumbersBS.started', showNumbersBS.tStart)
            showNumbersBS.maxDuration = None
            # keep track of which components have finished
            showNumbersBSComponents = showNumbersBS.components
            for thisComponent in showNumbersBS.components:
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
            # if trial has changed, end Routine now
            if isinstance(digitLoopBS, data.TrialHandler2) and thisDigitLoopBS.thisN != digitLoopBS.thisTrial.thisN:
                continueRoutine = False
            showNumbersBS.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 2.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fixationBS* updates
                
                # if fixationBS is starting this frame...
                if fixationBS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixationBS.frameNStart = frameN  # exact frame index
                    fixationBS.tStart = t  # local t and not account for scr refresh
                    fixationBS.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixationBS, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixationBS.started')
                    # update status
                    fixationBS.status = STARTED
                    fixationBS.setAutoDraw(True)
                
                # if fixationBS is active this frame...
                if fixationBS.status == STARTED:
                    # update params
                    pass
                
                # if fixationBS is stopping this frame...
                if fixationBS.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixationBS.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        fixationBS.tStop = t  # not accounting for scr refresh
                        fixationBS.tStopRefresh = tThisFlipGlobal  # on global time
                        fixationBS.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixationBS.stopped')
                        # update status
                        fixationBS.status = FINISHED
                        fixationBS.setAutoDraw(False)
                
                # *presentation_textBS* updates
                
                # if presentation_textBS is starting this frame...
                if presentation_textBS.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    presentation_textBS.frameNStart = frameN  # exact frame index
                    presentation_textBS.tStart = t  # local t and not account for scr refresh
                    presentation_textBS.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(presentation_textBS, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'presentation_textBS.started')
                    # update status
                    presentation_textBS.status = STARTED
                    presentation_textBS.setAutoDraw(True)
                
                # if presentation_textBS is active this frame...
                if presentation_textBS.status == STARTED:
                    # update params
                    pass
                
                # if presentation_textBS is stopping this frame...
                if presentation_textBS.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > presentation_textBS.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        presentation_textBS.tStop = t  # not accounting for scr refresh
                        presentation_textBS.tStopRefresh = tThisFlipGlobal  # on global time
                        presentation_textBS.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'presentation_textBS.stopped')
                        # update status
                        presentation_textBS.status = FINISHED
                        presentation_textBS.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    showNumbersBS.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in showNumbersBS.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "showNumbersBS" ---
            for thisComponent in showNumbersBS.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for showNumbersBS
            showNumbersBS.tStop = globalClock.getTime(format='float')
            showNumbersBS.tStopRefresh = tThisFlipGlobal
            thisExp.addData('showNumbersBS.stopped', showNumbersBS.tStop)
            # Run 'End Routine' code from getTmpNumberCodeBS
            thisExp.addData("digitsForTrial",digitsForTrial)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if showNumbersBS.maxDurationReached:
                routineTimer.addTime(-showNumbersBS.maxDuration)
            elif showNumbersBS.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-2.000000)
            thisExp.nextEntry()
            
        # completed digitSpan repeats of 'digitLoopBS'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "RecallBS" ---
        # create an object to store info about Routine RecallBS
        RecallBS = data.Routine(
            name='RecallBS',
            components=[recall_txtBS, textboxBS, cont_buttonBS, mouseBS],
        )
        RecallBS.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        textboxBS.reset()
        # setup some python lists for storing info about the mouseBS
        mouseBS.clicked_name = []
        gotValidClick = False  # until a click is received
        # store start times for RecallBS
        RecallBS.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        RecallBS.tStart = globalClock.getTime(format='float')
        RecallBS.status = STARTED
        thisExp.addData('RecallBS.started', RecallBS.tStart)
        RecallBS.maxDuration = None
        # keep track of which components have finished
        RecallBSComponents = RecallBS.components
        for thisComponent in RecallBS.components:
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
        # if trial has changed, end Routine now
        if isinstance(trialsBS, data.TrialHandler2) and thisTrialsBS.thisN != trialsBS.thisTrial.thisN:
            continueRoutine = False
        RecallBS.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *recall_txtBS* updates
            
            # if recall_txtBS is starting this frame...
            if recall_txtBS.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                recall_txtBS.frameNStart = frameN  # exact frame index
                recall_txtBS.tStart = t  # local t and not account for scr refresh
                recall_txtBS.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(recall_txtBS, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'recall_txtBS.started')
                # update status
                recall_txtBS.status = STARTED
                recall_txtBS.setAutoDraw(True)
            
            # if recall_txtBS is active this frame...
            if recall_txtBS.status == STARTED:
                # update params
                pass
            
            # *textboxBS* updates
            
            # if textboxBS is starting this frame...
            if textboxBS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textboxBS.frameNStart = frameN  # exact frame index
                textboxBS.tStart = t  # local t and not account for scr refresh
                textboxBS.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textboxBS, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textboxBS.started')
                # update status
                textboxBS.status = STARTED
                textboxBS.setAutoDraw(True)
            
            # if textboxBS is active this frame...
            if textboxBS.status == STARTED:
                # update params
                pass
            
            # *cont_buttonBS* updates
            
            # if cont_buttonBS is starting this frame...
            if cont_buttonBS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cont_buttonBS.frameNStart = frameN  # exact frame index
                cont_buttonBS.tStart = t  # local t and not account for scr refresh
                cont_buttonBS.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cont_buttonBS, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cont_buttonBS.started')
                # update status
                cont_buttonBS.status = STARTED
                cont_buttonBS.setAutoDraw(True)
            
            # if cont_buttonBS is active this frame...
            if cont_buttonBS.status == STARTED:
                # update params
                pass
            # *mouseBS* updates
            
            # if mouseBS is starting this frame...
            if mouseBS.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouseBS.frameNStart = frameN  # exact frame index
                mouseBS.tStart = t  # local t and not account for scr refresh
                mouseBS.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouseBS, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouseBS.started', t)
                # update status
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
                        clickableList = environmenttools.getFromNames(cont_button, namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouseBS):
                                gotValidClick = True
                                mouseBS.clicked_name.append(obj.name)
                        if not gotValidClick:
                            mouseBS.clicked_name.append(None)
                        if gotValidClick:  
                            continueRoutine = False  # end routine on response
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                RecallBS.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in RecallBS.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "RecallBS" ---
        for thisComponent in RecallBS.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for RecallBS
        RecallBS.tStop = globalClock.getTime(format='float')
        RecallBS.tStopRefresh = tThisFlipGlobal
        thisExp.addData('RecallBS.stopped', RecallBS.tStop)
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
            clickableList = environmenttools.getFromNames(cont_button, namespace=locals())
            for obj in clickableList:
                # is this object clicked on?
                if obj.contains(mouseBS):
                    gotValidClick = True
                    mouseBS.clicked_name.append(obj.name)
            if not gotValidClick:
                mouseBS.clicked_name.append(None)
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
        # create an object to store info about Routine FeedbackBS
        FeedbackBS = data.Routine(
            name='FeedbackBS',
            components=[feedback_textBS],
        )
        FeedbackBS.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        feedback_textBS.setText(fbTxt)
        # store start times for FeedbackBS
        FeedbackBS.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        FeedbackBS.tStart = globalClock.getTime(format='float')
        FeedbackBS.status = STARTED
        thisExp.addData('FeedbackBS.started', FeedbackBS.tStart)
        FeedbackBS.maxDuration = None
        # keep track of which components have finished
        FeedbackBSComponents = FeedbackBS.components
        for thisComponent in FeedbackBS.components:
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
        # if trial has changed, end Routine now
        if isinstance(trialsBS, data.TrialHandler2) and thisTrialsBS.thisN != trialsBS.thisTrial.thisN:
            continueRoutine = False
        FeedbackBS.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_textBS* updates
            
            # if feedback_textBS is starting this frame...
            if feedback_textBS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_textBS.frameNStart = frameN  # exact frame index
                feedback_textBS.tStart = t  # local t and not account for scr refresh
                feedback_textBS.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_textBS, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_textBS.started')
                # update status
                feedback_textBS.status = STARTED
                feedback_textBS.setAutoDraw(True)
            
            # if feedback_textBS is active this frame...
            if feedback_textBS.status == STARTED:
                # update params
                pass
            
            # if feedback_textBS is stopping this frame...
            if feedback_textBS.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_textBS.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_textBS.tStop = t  # not accounting for scr refresh
                    feedback_textBS.tStopRefresh = tThisFlipGlobal  # on global time
                    feedback_textBS.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_textBS.stopped')
                    # update status
                    feedback_textBS.status = FINISHED
                    feedback_textBS.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                FeedbackBS.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FeedbackBS.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "FeedbackBS" ---
        for thisComponent in FeedbackBS.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for FeedbackBS
        FeedbackBS.tStop = globalClock.getTime(format='float')
        FeedbackBS.tStopRefresh = tThisFlipGlobal
        thisExp.addData('FeedbackBS.stopped', FeedbackBS.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if FeedbackBS.maxDurationReached:
            routineTimer.addTime(-FeedbackBS.maxDuration)
        elif FeedbackBS.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trialsBS'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "End" ---
    # create an object to store info about Routine End
    End = data.Routine(
        name='End',
        components=[ThankYou],
    )
    End.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for End
    End.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    End.tStart = globalClock.getTime(format='float')
    End.status = STARTED
    thisExp.addData('End.started', End.tStart)
    End.maxDuration = None
    # keep track of which components have finished
    EndComponents = End.components
    for thisComponent in End.components:
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
    
    # --- Run Routine "End" ---
    End.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ThankYou* updates
        
        # if ThankYou is starting this frame...
        if ThankYou.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ThankYou.frameNStart = frameN  # exact frame index
            ThankYou.tStart = t  # local t and not account for scr refresh
            ThankYou.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ThankYou, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ThankYou.started')
            # update status
            ThankYou.status = STARTED
            ThankYou.setAutoDraw(True)
        
        # if ThankYou is active this frame...
        if ThankYou.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            End.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in End.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "End" ---
    for thisComponent in End.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for End
    End.tStop = globalClock.getTime(format='float')
    End.tStopRefresh = tThisFlipGlobal
    thisExp.addData('End.stopped', End.tStop)
    thisExp.nextEntry()
    # the Routine "End" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
