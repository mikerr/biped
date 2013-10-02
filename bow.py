#!/usr/bin/python
import time
import subprocess

# make list of 8 items
positions = [0] * 8

# set default positions

mid = 140
off = 0


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


time.sleep(1)

for step in range(1,500): # lean forward
        stepservo(lefthip,mid+40)
        stepservo(righthip,mid-40)

time.sleep(1)

for step in range(1,500):
        stepservo(lefthip,mid)
        stepservo(righthip,mid)

time.sleep(1)

for step in range(1,500): # lean back
         stepservo(lefthip,mid-30)
         stepservo(righthip,mid+30)

time.sleep(1)

for step in range(1,500):
        stepservo(lefthip,mid)
        stepservo(righthip,mid)


time.sleep(1)
for joint in range(1,7):
        servo(joint,mid)
time.sleep(1)
for joint in range(1,7):
        servo(joint,off)
		
