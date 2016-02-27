#!/usr/bin/python

import time
import RPi.GPIO as GPIO
import getopt, sys



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT, initial=GPIO.HIGH)



opts, args = getopt.getopt (sys.argv[1:], "of",["on","off"])
for opt, arg in opts:
   if opt in ("-o", "--on"):
       GPIO.output(22, GPIO.LOW)
       time.sleep(0.5)
       GPIO.output(22, GPIO.HIGH)
   elif opt in ("-f", "--off"):
       GPIO.output(22, GPIO.LOW)
       time.sleep(3)
       GPIO.output(22, GPIO.HIGH)





