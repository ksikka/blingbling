from getch.getch import getch
import time
import json

GEN_DATA = False

if GEN_DATA:

    print "Starting in 3"
    time.sleep(1)
    print "2"
    time.sleep(1)
    print "1"
    time.sleep(1)
    print "go"


    start = time.time()
    times = []

    while(1):
        current = time.time()
        t_off = current-start

        if t_off > 30:
            break

        x = getch()
        print x

        current = time.time()
        t_off = current-start

        times.append( t_off )

    print json.dumps(times)

else:
    files = ['s1', 's2', 's3', 's4', 's5']
    g_time_list = []
    for i, fname in enumerate( files ):
        with open(fname + '.json') as f:
            for t in json.load(f):
                g_time_list.append((t,i))

    g_time_list.sort(key=lambda x: x[1])

    print json.dumps(g_time_list)
