# import GUI
import threading
import RPi.GPIO as GPIO
from motorContor import StepMotor

RLmotor = StepMotor(2,3,4,14)
RLmotor.run_degree(20)
GPIO.cleanup()