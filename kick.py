#!/usr/bin/python
import time
import subprocess

# set default positions

mid = 140
off = 0


# make list of 8 items
positions = [0] * 8

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
        if (position == 0): position = 140
	positions[joint] = position


for joint in range(0,8):
        servo(joint,mid)
time.sleep(1)
# begin movements


for step in range(1,200): 
        stepservo(leftankle,mid-30)
for step in range(1,200): 
        stepservo(rightankle,mid-15)

# super speed kick:

servo(lefthip,mid+30)
servo(leftknee,mid-50)

time.sleep(0.2)

# put leg down again
servo(leftankle,mid)
servo(rightankle,mid)
servo(lefthip,mid)
servo(leftknee,mid)
for step in range(1,200): 
	stepservo(lefthip,mid)
	stepservo(leftknee,mid)

# restore to neutral 
for step in range(1,200): 
	for joint in range(0,8):
        	stepservo(joint,mid)

time.sleep(1)
# switch off servos
for joint in range(0,8):
        servo(joint,off)
		
