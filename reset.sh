#!/bin/sh

mid=140
off=0

rightankle=2
leftankle=3
rightknee=4
leftknee=5
righthip=6
lefthip=7

d=0.9

joints()
{
  echo $leftankle=$1 > /dev/servoblaster
  echo $rightankle=$2 > /dev/servoblaster

  echo $leftknee=$3 > /dev/servoblaster
  echo $rightknee=$4 > /dev/servoblaster

  echo $lefthip=$5 > /dev/servoblaster
  echo $righthip=$6 > /dev/servoblaster

  sleep $d
}


# center joints & turn off
joints  $mid $mid $mid $mid $mid $mid

joints 0 0 0 0 0 0
