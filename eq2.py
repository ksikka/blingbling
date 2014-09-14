
# coding: utf-8

# In[1]:

#get_ipython().magic(u'matplotlib inline')

import math
import os
import sys
import numpy as np
import librosa
import matplotlib.pyplot as plt
import IPython.display


# In[26]:

audio_path = "hurtz.mp3"
audio_path = "justice-dance.mp3"
audio_path = "trololo.mp3"
audio_path = "turn-down-for-what.mp3"

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

