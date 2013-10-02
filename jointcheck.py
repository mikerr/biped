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

# center 

for joint in range(0,8):
	servo(joint,mid)

# begin movements

for joint in range(0,8):
	print joint,
	servo(joint,mid-10)
	time.sleep(1)
	servo(joint,mid)
	time.sleep(1)

	print "\n"

time.sleep(1)

for joint in range(0,8):
        servo(joint,off)
		
