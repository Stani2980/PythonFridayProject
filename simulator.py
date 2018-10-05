"""
This script simulates network traffic to a given URL

Usage $python simulator.py <url> <number of requests>
"""

import requests
import time
import sys
import logging
from multiprocessing import Pool, Process, Lock


# time_to_wait = 2
        
def make_request(l, count):
    logging.basicConfig(filename='info.log', level=logging.INFO)
    epoch_time_before = time.time()
    response = requests.get(sys.argv[1]) # url to ping
    if response.status_code == 200:
        epoch_time_after = time.time()
        l.acquire()
        logging.log(logging.INFO, "It took " + str(epoch_time_after - epoch_time_before) + " seconds to perform this request. Process: " + str(count))
        print(f'Process: {count}')
        l.release()

if __name__ == '__main__':
        lock = Lock()
        
        for i in range(int(sys.argv[2])):
            Process(target=make_request, args=(lock,i)).start()
        

