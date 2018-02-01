#VR Motion Simulator
#By: Yousuf A

import onionGpio
from time import sleep
import sys
import os

potPin=3


off=0
on=1

pot=onionGpio.OnionGpio(potPin)
pot._freeGpio()
pot.setOutputDirection(0)
sleep(2)

pot.setInputDirection()

count=0
potential=pot.getValue()

print("VR Motion Simulator")
print("By: Yousuf A")

while (1):
 pot=onionGpio.OnionGpio(potPin)
 #Clear capacitor
 pot.setOutputDirection(0)
 sleep(1)
 pot.setInputDirection()

 while (int(pot.getValue())==0):
  count+=1
 print (count)
 if (count/2)>100:
  count=100
 #Output value obtained to device
 os.system('fast-gpio pwm 0 500 '+str(count/10))
 count=0

print("By: Yousuf A")
