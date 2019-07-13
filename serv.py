from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time
import serial
import random
import asyncio
import RPi.GPIO as GPIO
from smbus2 import SMBus

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
 
 
@app.route('/')
def index(name=None):
    return render_template('index.html', name=name)


@socketio.on('menssagem')
def potencia(data):    
    # Open i2c bus 1 and read one byte from address 80, offset 0
    bus = SMBus(1)   
    tensaoStr=''
    correnteStr= ''
    while True:
        
        tensaoArray = bus.read_i2c_block_data(0x18,0,6)
        correnteArray = bus.read_i2c_block_data(0x17,0,6)
        for i in range(6):
            tensaoStr += chr(tensaoArray[i])
            correnteStr += chr(correnteArray[i])
            time.sleep(0.1)
        
        
       
        tensao=float(tensaoStr)
        corrente=float(correnteStr)
        round(corrente, 3)
        potencia = tensao*corrente
        pot = round(potencia, 3)
        print('V:',tensao)
        print('A:',corrente)
        print('W: ',pot)
        print(data)                     
        emit('menssagem2', pot)
        tensaoStr = ''
        correnteStr =''
        




          
if __name__ == '__main__':
    socketio.run(app, debug = True, host='0.0.0.0')