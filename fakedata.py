import time
import json
import sys

GEN_DATA = False
if len(sys.argv) > 1:
    #print sys.argv
    gen_data = sys.argv[1]
    GENDATA = gen_data == 'gendata'

if GEN_DATA:
    from getch.getch import getch

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
    files = ['onsets-1', 'onsets-2', 'onsets-3', 'onsets-4', 'onsets-5']
    g_time_list = []
    for i, fname in enumerate( files ):
        """
        with open(fname + '.json') as f:
            for t in json.load(f):
                g_time_list.append((t,i))
                """
        with open(fname) as f:
            for line in f.readlines():
                if line.strip() != "":
                    g_time_list.append((float(line.strip()),i))

    g_time_list.sort(key=lambda x: x[0])

    print json.dumps(g_time_list)
