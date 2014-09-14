
import time
import serial
import os

start = time.time()
f = open('realdata.json','r')
beats = eval(f.read())
ser = serial.Serial('/dev/tty.usbserial-AH02M63N',9600)
visited = []
i = 0
print(beats)

import threading
import time

def play_song(songname):
    return os.system('afplay ' + songname)

t = threading.Thread(target=play_song, args=("turn-down-for-what.mp3",))
t.start()
while(1):
	for beat in beats[i:]:
		current = time.time()
		if current - start > beat[0]:
			if beat not in visited:
				visited.append(beat)
				i += 1
				print(beat[0])
				ser.write(str(beat[1]))
t.join()


