
# coding: utf-8

# In[1]:

#get_ipython().magic(u'matplotlib inline')

import os

import numpy as np

import librosa

import matplotlib.pyplot as plt

import IPython.display


# In[26]:

audio_path = "justice-dance.mp3"

y, sr = librosa.load(audio_path, sr=22050)


# In[27]:

IPython.display.Audio(data=y, rate=sr)


# In[28]:

S = librosa.feature.melspectrogram(y, sr=sr, n_fft=2048, hop_length=64, n_mels=128)
log_S = librosa.logamplitude(S, ref_power=np.max)

y_harmonic, y_percussive = librosa.effects.hpss(y)


# In[29]:

IPython.display.Audio(data=y_harmonic, rate=sr)


# In[30]:

IPython.display.Audio(data=y_percussive, rate=sr)


# In[63]:

tempo, beats = librosa.beat.beat_track(y=y_percussive, sr=sr)

plt.figure(figsize=(12,4))
librosa.display.specshow(log_S, sr=sr, hop_length=64, x_axis='time', y_axis='mel')

plt.vlines(beats, 0, log_S.shape[0], colors='k', linestyles='-', linewidth=2.5)
plt.vlines(beats, 0, log_S.shape[0], colors='w', linestyles='-', linewidth=1.5)

plt.axis('tight')
plt.tight_layout()


# In[64]:

n = 100

print 'Estimated tempo:        %.2f BPM' % tempo
print 'First %d beat frames:\n' % n, beats[:n]

beat_times = librosa.frames_to_time(beats[:n], sr=sr)
print 'First %d beat times:\n' % n, beat_times

print 'Saving in beattimes.json'
import json
with open('beattimes.json', 'w') as f:
    json.dump(beat_times.tolist(), f)
