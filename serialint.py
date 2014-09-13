
import time
import serial

start = time.time()
f = open('beat.txt','r')
beats = eval(f.read())
ser = serial.Serial('/dev/tty.usbserial-AH02M63N',9600)
visited = []

while(1):
	for beat in beats:
		current = time.time()
		if current - start > beat:
			if beat not in visited:
				visited.append(beat)
				print(beat)
				ser.write('5')