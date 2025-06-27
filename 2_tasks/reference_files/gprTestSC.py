import os
import sys
from psychopy import core

from psychopy.parallel import ParallelPort
port = ParallelPort(address = 0xD010) # 0xD010 is the address of the parallel port
port.setData(0) # zero out the value in case it's not

# Proof of concept for use:
# The following code sends markers to Biopac 
# as if there are two events, each 1s long,
# separated by 2s.

port.setData(1) # set marker on
core.wait(1)
port.setData(0) # set marker off

core.wait(2)

port.setData(1)
core.wait(1)
port.setData(0)





# MATLAB CODE USED FOR INSPIRATION/ASSISTANCE
# function [ sudjdata ] = vicTest( subID )
# %testing biopac markiing for vic
#
#nT = 5;
# % Zero the parallel port, just need to do once in this script
#
# adOut = hex2dec('D010');
# %adIn = adOut + 1;
# config_io;
# outp(adOut,0);
# 
#for i = 1:nT
#    outp(adOut, 1);
#    disp({'TEST'})
#    pause(.5)
#    outp(adOut, 0);
#    pause(1)
#end
#
#clear all
#
#end
