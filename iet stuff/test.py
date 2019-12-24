import serial
from time import sleep
words = serial.Serial('com4',9600)


while True:
	words.write(('str' + '\n').encode('UTF-8'))
	sleep(1)
	words.write('boo'.encode())
	sleep(1)
	words.write('boo'.encode())
	sleep(1)