import serial
import time
import timeit 

def potencia():
    ser3 = serial.Serial('/dev/ttyACM0', 115200)
    #ser4 = serial.Serial('/dev/ttyACM1', 9600)
    for i in range(50):
        time.sleep(0.2)
        tensao = float(ser3.readline().strip())
        #time.sleep(0.1)
        #corrente = float(ser4.readline().strip())
        #potencia= corrente * tensao
        #print('corrente:', corrente)
        print('tensao:' , tensao)
potencia()  
