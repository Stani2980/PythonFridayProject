"""
This script simulates network traffic to a given URL

Usage $python simulator.py <url> <number of requests>
"""

import requests
import time 
import numpy as np
import sys
import logging
from multiprocessing import Pool, Manager, Lock, current_process, Process
from datetime import datetime, date


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

def make_request_globallock(count):
    logging.basicConfig(filename='info.log', level=logging.INFO)
    
    for _ in range(count[0]):
        epoch_time = time.time() # start timer
        #response = requests.get(sys.argv[1]) # url to ping
        epoch_time = time.time() - epoch_time  # stop timer
        lock.acquire()
        #status = response.status_code
        created = "hi"


        status = created
        timestamp = datetime.now()
        logging.log(logging.INFO, f' Timestamp: {timestamp} - Status code: {status} - Epoch for request in sec: {epoch_time}')
        lock.release()


def generate_freq(amount):
    delta = np.random.uniform(-10, 10, size=(amount,))
    res = .4 * np.arange(amount) ** 2 + 3 + delta + 10
    return res.tolist()


def init(l):
    global lock
    lock = l


if __name__ == '__main__':
        
        l = Lock()
        floatlist = generate_freq(int(sys.argv[2]))
        mylist = [[int(num)] for num in floatlist]   

        pool = Pool(initializer=init, initargs=(l,))
        pool.map(make_request_globallock, mylist)
        pool.close()
        pool.join()
            

