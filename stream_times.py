import json
with open('beattimes.json') as f:
    beat_times = json.load(f)

# stream bytes on this schedules
f = open("beat.txt","w")
print >> f, beat_times
print beat_times
