import json
with open('beattimes.json') as f:
    beat_times = json.load(f)

# stream bytes on this schedules
print beat_times
