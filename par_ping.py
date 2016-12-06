#!/usr/bin/env python

import sys
import os
import subprocess
import multiprocessing

INPUT_FILE = './hosts'
NUM_PROC = int(sys.argv[1])


def ping(pid):
    print("pid: ", os.getpid())
    #for i in list:
    #    print(i)
    print("waiting some second...")
    subprocess.call("sleep 10", shell=False)

def init():
    # Read the hosts list into a list
    hosts = []
    f = open(INPUT_FILE, 'r')
    for line in f.readlines():
        hosts.append(line.strip())
    
    # Calculate the data portions
    num_hosts = len(hosts)
    offset = num_hosts // NUM_PROC
    tail = num_hosts % NUM_PROC

    # Return the arguments
    return hosts, num_hosts, offset, tail

    # # Spawn the ping childs
    # for p in range(NUM_PROC):
    #     if p == (NUM_PROC-1):
    #         subprocess.run(ping(p, hosts[offset*p : offset*(p+1)+tail]))
    #     else:
    #         subprocess.run(ping(p, hosts[offset*p : offset*(p+1)]))

if __name__ == "__main__":
    hosts = []
    hosts, num_hosts, offset, tail = init()
    pool = multiprocessing.Pool(processes=NUM_PROC)
    r = pool.map_async(ping, [1, 2, 3])
    r.wait()
