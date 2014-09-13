
import time
import serial
import sound


s = Sound() 
s.read('sound.wav') 


start = time.time()
f = open('beat.txt','r')
beats = eval(f.read())
ser = serial.Serial('/dev/tty.usbserial-AH02M63N',9600)
visited = []
i = 0

s.play()
while(1):
	for beat in beats[i:]:
		current = time.time()
		if current - start > beat:
			if beat not in visited:
				visited.append(beat)
				i += 1
				print(beat)
				ser.write('5')