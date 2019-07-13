import serial
comunicacaoSerial = serial.Serial('/dev/ttyAMA0', 115200)
	
while 1 :
  print (comunicacaoSerial.readline())
