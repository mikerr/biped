#!/usr/bin/python
import time
import subprocess


# set default positions

mid = 140
off = 0

# make list of 8 items
positions = [mid] * 8

rightankle = 2
leftankle = 3
righthip = 4
leftknee = 5
rightknee = 6
lefthip  = 7


def stepservo(joint,endpos):
        startpos = positions[joint]
        step = 1
        if endpos < startpos:
                step = -step

        if startpos != endpos:
                position = startpos + step
                servo(joint,position)

def servo(joint,position):
        command = "echo " + str (joint) + "=" + str(position)
        command += ">/dev/servoblaster"
        subprocess.call (command, shell=True)
        positions[joint] = position

# center 

for joint in range(0,8):
	servo(joint,mid)

		
