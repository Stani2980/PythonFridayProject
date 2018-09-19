"""
This script simulates network traffic to a given URL

Usage $python simulator.py [<url>]
"""

import requests
import time
import sys
import logging
from multiprocessing import Pool, Process


# time_to_wait = 2
        
def make_request(count):
    logging.basicConfig(filename='info.log', level=logging.INFO)
    epoch_time_before = time.time()
    response = requests.get(sys.argv[1]) # url to ping
    if response.status_code == 200:
        epoch_time_after = time.time()
        logging.log(logging.INFO, "It took " + str(epoch_time_after - epoch_time_before) + " seconds to perform this request. Process: " + str(count))
        print(f'Process: {count}')


if _name_ == '_main_':
    for i in range(1, int(sys.argv[2])): # amount of requests
        ##with Pool(4) as pool:
        ##  pool.map(make_request, [])

        p = Process(target=make_request, args=([i]))
        p.start()