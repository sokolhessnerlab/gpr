#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 15:01:47 2022

@author: shlab
"""


'''
testing hovering mouse over slider to make rating
'''

# Import modules we need
import random, time, os
import pandas as pd
from psychopy import visual, core, event, monitors
from psychopy.hardware import keyboard
import numpy as np

# change directory
#os.chdir('/Users/hayley/Documents/Github/rcs/rdmTask') # hb mac
os.chdir('/Users/shlab/Documents/Github/rcs/rdmTask') # mahimahi
#os.chdir('/Users/Display/Desktop/Github/rcs/rdmTask') # tofu



  

# Set up the experimental parameters that are consistent across task rounds:

# Screen dimensions and drawing stuff
#scrnsize= [800,800] #how large the screen will be
#scrnsize=[1280,1024] # CORRECT DIMENSIONS FOR REAL TASK
scrnsize = [1024,819.2] # 80% of correct size for mac laptop
center = [0,100]
centerR = [scrnsize[0]/4,100]
centerL = [scrnsize[0]/-4,100]
radius = scrnsize[0]/5.5
rectHeight = radius +2 #rectangle used to cover up half the circle when outcome is gain or loss
rectWidth = radius*2+2
#textHeight = radius/2.1
textHeight = 40
moneyTextHeight= textHeight*2
wrap = scrnsize[0]*.9 # text wrapping
 
# Set up the window
win = visual.Window(
    size=scrnsize,
    units="pix",
    fullscr=False,
    color=[-1, -1, -1], #black screen
    screen=1 # on second screen
)

sliderLockPostQ= visual.TextStim( # rating recorded
    win, 
    pos = (0,scrnsize[1]*-.45),
    color=[.5,0,.5],
    height = textHeight*.8,
    wrapWidth = wrap,
    alignText="center",
    text="Rating recorded!"
)

# set color of marker and repsonse recorded text

sliderColor=[.5,0,.5] # purple

# For some reason, slider.labels is not showing up dynamically, so we reset it here to make labels fit the question
slider = visual.Slider(
    win, 
    size=(scrnsize[0]*.8, 50), 
    pos=(0, scrnsize[1]*-.25),
    labels = ['Very \neasy', 'Very \ndifficult'],
    ticks = [1,100],
    granularity=0, 
    style=['rating'],
    color=sliderColor, 
    font='Helvetica',
    labelHeight=30,
)


    

slider_width = 992
slider_height = 50
slider_orientation = 0
slider_ticks = [0,100]
slider_labels = ['Very \neasy', 'Very \ndifficult']
slider_granularity = .1
slider_decimals = 1
slideSpeed=3
oldRating = 50
sliding = 0


slider_shape = visual.Rect(
    win=win, name='slider_shape',
    width=(slider_width, slider_height)[0], height=(slider_width, slider_height)[1],
    ori=0, pos=slider.pos,
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True
)

 
slider.markerPos = 50
slider.marker.color = sliderColor
slider_shape.draw()
slider.draw()

win.flip()

mouse = event.Mouse(visible = True, win = win) 
mouseRec=mouse.getPos()



continueRout=True
while continueRout:
    
    if slider.markerPos and mouse.isPressedIn(slider_shape):
        continueRout = False
    elif slider_shape.contains(mouse) and mouse.getPos()[slider_orientation] != mouseRec[slider_orientation]:
        mouseRec=mouse.getPos()
        slider.markerPos=mouseRec[slider_orientation]/slider_width*(slider_ticks[-1]-slider_ticks[0])+(slider_ticks[0]+slider_ticks[-1])/2
        sliding = 0
        slider_shape.draw()
        slider.draw()
        win.flip()


core.wait(1)
win.close()
