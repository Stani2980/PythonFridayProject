"""
This script simulates network traffic to a given URL

Usage $python simulator.py <url> <number of requests>
"""

import requests
import time 
import numpy as np
import os
import sys
import logging
from multiprocessing import Pool, Manager, Lock, Process
from datetime import datetime, date


def work_ordered_by_pooler(count):
    logging.basicConfig(filename='info.log', level=logging.INFO)
    
    for _ in range(count[0]):
        pid = str(os.getpid())
        pid = pid[3:]
        ppid = os.getppid()
        lock.acquire()
        logging.log(logging.INFO, f' Iteration no.: {_ + 1}, MAX iterations: {count[0]} - pid: {pid}, ppid: {ppid}')
        lock.release()


def work_in_sorted_order(count):
    logging.basicConfig(filename='info.log', level=logging.INFO)
    lock.acquire()
    for _ in range(count[0]):
        pid = str(os.getpid())
        pid = pid[3:]
        ppid = os.getppid()
        logging.log(logging.INFO, f' Iteration no.: {_ + 1}, MAX iterations: {count[0]} - pid: {pid}, ppid: {ppid}')

    logging.log(logging.INFO, f'')
    lock.release()


def generate_freq(amount):
    res = np.arange(1,amount+1)

    return res.tolist()


def init(l):
    global lock
    lock = l


if __name__ == '__main__':
    l = Lock()
    floatlist = generate_freq(int(sys.argv[1]))
    
    mylist = [[int(num)] for num in floatlist]   
    pool = Pool(initializer=init, initargs=(l,))
    pool.map(work_in_sorted_order, mylist)
    pool.close()
    pool.join()
            

