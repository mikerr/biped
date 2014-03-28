#!/usr/bin/python
import time
import subprocess

# fastwalk.py 
# 13 seconds / 8 steps / 30cm

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
        positions[joint] = position


# center all servos

for joint in range(0,8):
        servo(joint,mid)

time.sleep(1)

# do 10 strides
for x in range (1,5):

	# length of stride 
        leftstride = 25
        rightstride = 20

        #left side

        #lean left

        for step in range(1,100):
                stepservo(leftankle,mid+30)
                stepservo(rightankle,mid+30)


        # lift right leg

	#time.sleep(0.1)
        servo(righthip,mid-rightstride)

        #centre

        for step in range(1,100):
                stepservo(leftankle,mid)
                stepservo(rightankle,mid)

        # drop right leg

        servo(righthip,mid)

# right side

        # lean right

        for step in range(1,100):
                stepservo(rightankle,mid-15)
                stepservo(leftankle,mid-15)

        # lift left leg

	#time.sleep(0.1)
	# fast leg
        servo(lefthip,mid+leftstride)

        #lean left

        for step in range(1,100):
                stepservo(leftankle,mid)
                stepservo(rightankle,mid)

        # drop right leg

        servo(lefthip,mid)

# END

# back to neutral

for joint in range(0,8):
        servo(joint,mid)

time.sleep(0.5)

# turn off
for joint in range(0,8):
        servo(joint,off)
		
time.sleep(0.5)

