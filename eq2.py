
# coding: utf-8

# In[1]:

#get_ipython().magic(u'matplotlib inline')

import math
import os
import sys

GENDATA = False
if len(sys.argv) > 1:
    #print sys.argv
    gen_data = sys.argv[1]
    GENDATA = gen_data == 'gendata'


audio_path = "hurtz.mp3"
audio_path = "justice-dance.mp3"
audio_path = "trololo.mp3"
audio_path = "turn-down-for-what.mp3"
output_csv = "onsets"

import threading
import time

def play_song(songname):
    return os.system('afplay ' + songname)

if not GENDATA:
    t = threading.Thread(target=play_song, args=(audio_path,))
    t.start()

    start = time.time()

    with open(output_csv) as f:
        times = [float(s.strip()) for s in f.readlines() if s.strip() != ""]

    for t in sorted(times):
        current = time.time()
        t_off = current - start
        time.sleep(t - t_off)
        print t

    t.join()
else:
    import numpy as np
    import librosa
    import matplotlib.pyplot as plt
    import IPython.display
    # 1. load the wav file and resample to 22.050 KHz
    print 'Loading ', audio_path
    y, sr = librosa.load(audio_path, sr=22050)

    # Use a default hop size of 64 frames @ 22KHz ~= 11.6ms
    hop_length = 64

    # This is the window length used by default in stft
    n_fft = 2048

    print 'Splitting into harmonic and percussion ...'
    y_harm, y_perc = librosa.effects.hpss(y)

    configs = [(.06, y_harm)
             , (.12, y_harm)
             , (0.2, y_perc)
             , (0.28, y_perc)
             ]

    # 2. run onset detection
    for i in xrange(4):
        delta, sound_wave = configs[i]
        print 'Detecting onsets with delta = ' + str(delta) + ' ...'
        onsets = librosa.onset.onset_detect(y=sound_wave,
                                            sr=sr,
                                            hop_length=hop_length,
                                            delta=delta)

        print "Found {} onsets.".format(onsets.shape[0])

        # 3. save output
        # 'beats' will contain the frame numbers of beat events.

        onset_times = librosa.frames_to_time(onsets,
                                             sr=sr,
                                             hop_length=hop_length,
                                             n_fft=n_fft)

        print 'Saving output to ', output_csv
        librosa.output.times_csv(output_csv+'-%d'%(i+1), onset_times)
    print 'done!'

sys.exit(0)

""" PREVIOUS JUnK """
y, sr = librosa.load(audio_path, sr=22050)
x = np.abs(librosa.stft(y))
axes = librosa.display.specshow(x)
axes.write_png('test/long4.png')
sys.exit(1)
"""
print y.shape

print y[50]
os.exit(0)

#x = np.abs(librosa.stft(y[:20*22050]))
"""
x = np.abs(librosa.stft(y[:160*22050]))
print x.shape


import time

print "Starting in 3"
time.sleep(1)
print "2"
time.sleep(1)
print "1"
time.sleep(1)
print "go"

freq_range = [i / 16 * 1024 for i in [.05,.12,.33,.5,1,1,2,3,3,5]]
freq_range = [i / 16 * 1024 for i in [.05,.12,.33,.5,.6,.8,1.6,3,4,5]]

def get_freq_intensity_vector(col):
    # the column is 1 fft column
    bucket_vals = []
    col_index = 0
    for num_elements in freq_range:
        val = 0
        for i in xrange(int(num_elements)):
            col[i]
            val += col[i]
            col_index += 1
        bucket_vals.append(val)
    return bucket_vals

# x.shape[1] / 60 is approximately 43 (ticks per second)
# print the new values every 1/10 seconds.
t_interval = int( x.shape[1] / 60 * 0.1 )
print "interval is " + str(t_interval)
# buffer up data for 100ms
cols = []
for t,col in enumerate(x):
    if (t+1) % t_interval == 0:
        print "t = %d" % (t/t_interval)

        sum_buckets = get_freq_intensity_vector(col)
        for col2 in cols:
            sum_buckets = [ s + bv for s,bv in zip(sum_buckets,col2)]

        print [int(math.sqrt(i+1)) for i in sum_buckets]
        time.sleep(.1)
        cols = []
    else:
        cols.append(get_freq_intensity_vector(col))

sys.exit(0)

axes = librosa.display.specshow(x)
axes.write_png('test/long.png')

sys.exit(0)

y_harmonic, y_percussive = librosa.effects.hpss(y)

