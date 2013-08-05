import time
import subprocess


# set default positions

mid = 140
off = 0


# make list of 7 items
positions = [mid] * 7

rightankle = 1
leftankle = 2
righthip = 3
leftknee = 4
rightknee = 5
lefthip  = 6

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


for joint in range(1,7):
        servo(joint,mid)
time.sleep(1)
# begin movements


for step in range(1,200): 
        stepservo(leftankle,mid-30)
for step in range(1,200): 
        stepservo(rightankle,mid-10)

# super speed kick:

servo(righthip,mid+50)
servo(leftknee,mid-50)
time.sleep(0.2)
servo(leftknee,mid)
servo(leftankle,mid)

time.sleep(0.2)
for step in range(1,200): 
	stepservo(righthip,mid)

# restore to neutral 
for step in range(1,200): 
	for joint in range(1,7):
        	stepservo(joint,mid)

time.sleep(1)
# switch off servos
for joint in range(1,7):
        servo(joint,off)
		
