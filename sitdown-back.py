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
rightknee = 4
leftknee = 5
righthip = 6
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



# begin movements

for joint in range(0,8):
        servo(joint,mid)

# lean torso back

for step in range(1,500): 
        stepservo(lefthip,mid-100)
        stepservo(righthip,mid+100)

# bend knees forward

for step in range(1,500): 
        stepservo(leftknee,mid-100)
        stepservo(rightknee,mid+100)

# Now sitting down - wait a bit
time.sleep(4)

# straigten knees
for step in range(1,500): 
        stepservo(leftknee,mid)
        stepservo(rightknee,mid)


# torso to neutral
for step in range(1,500): 
        stepservo(lefthip,mid)
        stepservo(righthip,mid)


time.sleep(1)
for joint in range(0,8):
        servo(joint,off)
		
time.sleep(1)
