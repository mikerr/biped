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


# center all servos

for joint in range(1,7):
        servo(joint,mid)

time.sleep(1)

# begin movements


# lean forward

for step in range(1,500): 
        stepservo(lefthip,mid+100)
        stepservo(righthip,mid-100)


# lean back

for step in range(1,500): # lean back
         stepservo(lefthip,mid-100)
         stepservo(righthip,mid+100)


# center
for step in range(1,500):
        stepservo(lefthip,mid)
        stepservo(righthip,mid)

time.sleep(1)
for joint in range(1,7):
        servo(joint,mid)
time.sleep(1)
for joint in range(1,7):
        servo(joint,off)
		
time.sleep(1)
