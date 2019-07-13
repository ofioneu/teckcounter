import serial
import time
import RPi.GPIO as GPIO

ser4 = serial.Serial('/dev/serial0', 115200)

for i in range(100):
        
        corrente = float(ser4.readline().strip())
        time.sleep(0.5)  
        print('corrente:', corrente)
        
