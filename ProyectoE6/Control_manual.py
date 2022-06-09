import sys
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Ingresar valores al INT
grados = int(input("ingrese cantidad en Grados:"))

#Declaracion de variables

pin1 = 11
pin2 = 13
pin3 = 12
pin4 = 15
WaitTime = int(1 / float(1000)
iDeg = int(grados * 11.377777777777)

#Declaracion de pines

GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)





def Derecha
	GPIO.output(pin1, GPIO.HIGH)
	GPIO.output(pin2, GPIO.LOW)
	GPIO.output(pin3, GPIO.LOW)
	GPIO.output(pin4, GPIO.HIGH)
	time.sleep(WaitTime)
	GPIO.output(pin1, GPIO.HIGH)
	GPIO.output(pin2, GPIO.LOW)
	GPIO.output(pin3, GPIO.LOW)
	GPIO.output(pin4, GPIO.LOW)
	time.sleep(WaitTime)
	GPIO.output(pin1, GPIO.HIGH)
	GPIO.output(pin2, GPIO.HIGH)
	GPIO.output(pin3, GPIO.LOW)
	GPIO.output(pin4, GPIO.LOW)
	time.sleep(WaitTime)
	GPIO.output(pin1, GPIO.LOW)
	GPIO.output(pin2, GPIO.HIGH)
	GPIO.output(pin3, GPIO.LOW)
	GPIO.output(pin4, GPIO.LOW)
	time.sleep(WaitTime)
	GPIO.output(pin1, GPIO.LOW)
	GPIO.output(pin2, GPIO.HIGH)
	GPIO.output(pin3, GPIO.HIGH)
	GPIO.output(pin4, GPIO.LOW)
	time.sleep(WaitTime)
	GPIO.output(pin1, GPIO.LOW)
	GPIO.output(pin2, GPIO.LOW)
	GPIO.output(pin3, GPIO.HIGH)
	GPIO.output(pin4, GPIO.LOW)
	time.sleep(WaitTime)
	GPIO.output(pin1, GPIO.LOW)
	GPIO.output(pin2, GPIO.LOW)
	GPIO.output(pin3, GPIO.HIGH)
	GPIO.output(pin4, GPIO.HIGH)
	time.sleep(WaitTime)
	GPIO.output(pin1, GPIO.LOW)
	GPIO.output(pin2, GPIO.LOW)
	GPIO.output(pin3, GPIO.LOW)
	GPIO.output(pin4, GPIO.HIGH)
	time.sleep(WaitTime)

def Izquierda
	GPIO.output(pin1, GPIO.LOW)
	GPIO.output(pin2, GPIO.HIGH)
	GPIO.output(pin3, GPIO.HIGH)
	GPIO.output(pin4, GPIO.LOW)
	time.sleep(WaitTime)
	GPIO.output(pin1, GPIO.LOW)
	GPIO.output(pin2, GPIO.HIGH)
	GPIO.output(pin3, GPIO.HIGH)
	GPIO.output(pin4, GPIO.HIGH)
	time.sleep(WaitTime)
	GPIO.output(pin1, GPIO.LOW)
	GPIO.output(pin2, GPIO.LOW)
	GPIO.output(pin3, GPIO.HIGH)
	GPIO.output(pin4, GPIO.HIGH)
	time.sleep(WaitTime)
	GPIO.output(pin1, GPIO.HIGH)
	GPIO.output(pin2, GPIO.LOW)
	GPIO.output(pin3, GPIO.HIGH)
	GPIO.output(pin4, GPIO.HIGH)
	time.sleep(WaitTime)
	GPIO.output(pin1, GPIO.HIGH)
	GPIO.output(pin2, GPIO.LOW)
	GPIO.output(pin3, GPIO.LOW)
	GPIO.output(pin4, GPIO.HIGH)
	time.sleep(WaitTime)
	GPIO.output(pin1, GPIO.HIGH)
	GPIO.output(pin2, GPIO.HIGH)
	GPIO.output(pin3, GPIO.LOW)
	GPIO.output(pin4, GPIO.HIGH)
	time.sleep(WaitTime)
	GPIO.output(pin1, GPIO.HIGH)
	GPIO.output(pin2, GPIO.HIGH)
	GPIO.output(pin3, GPIO.LOW)
	GPIO.output(pin4, GPIO.LOW)
	time.sleep(WaitTime)
	GPIO.output(pin1, GPIO.HIGH)
	GPIO.output(pin2, GPIO.HIGH)
	GPIO.output(pin3, GPIO.HIGH)
	GPIO.output(pin4, GPIO.LOW)
	time.sleep(WaitTime)

def Reposo
	GPIO.output(pin1, GPIO.LOW)
	GPIO.output(pin2, GPIO.LOW)
	GPIO.output(pin3, GPIO.LOW)
	GPIO.output(pin4, GPIO.LOW)
