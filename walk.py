import time
import subprocess

# make list of 7 items
positions = [0] * 7

# set default positions

mid = 140
off = 0


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
        positions[joint] = position


# center all servos

for joint in range(1,7):
        servo(joint,mid)

time.sleep(1)


for x in range (1,9):


        leftstride = 20
        rightstride = 20

        #left side

        #lean left

        for step in range(1,500):
                stepservo(leftankle,mid+30)
                stepservo(rightankle,mid+30)


        # lift right leg


        for step in range(1,500):
                stepservo(righthip,mid-rightstride)
                stepservo(rightknee,mid-00)

        #centre

        for step in range(1,500):
                stepservo(leftankle,mid)
                stepservo(rightankle,mid)

        # drop right leg

        for step in range(1,500):
                stepservo(righthip,mid)
                stepservo(rightknee,mid)

# rigth side

        # lean right

        for step in range(1,500):
                stepservo(leftankle,mid-15)
                stepservo(rightankle,mid-15)

        # lift left leg

        for step in range(1,500):
                stepservo(lefthip,mid+leftstride)
                stepservo(leftknee,mid+0)

        #lean left

        for step in range(1,500):
                stepservo(leftankle,mid)
                stepservo(rightankle,mid)

        # drop right leg

        for step in range(1,500):
                stepservo(lefthip,mid)
                stepservo(leftknee,mid)

# END

# back to neutral

for joint in range(1,7):
        servo(joint,mid)

time.sleep(0.5)

# turn off
for joint in range(1,7):
        servo(joint,off)
		

