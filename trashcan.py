#!/usr/bin/env python

from threading import Thread
import numpy as np
import time
import requests
import os

def simulate(cap, lamb, sleep):
    """
    Simulate a trash can with a poisson distribution with parameter lam.
    Sleeps for `sleep` seconds between each count.
    After `cap` capacity is reached, then trash can is full and stop.
    """
    count = 0
    while count < cap:
        # Generate one value with lambda as parameter
        val = np.random.poisson(lamb)
        count += val
        time.sleep(sleep)
    return True

def simAndAlert(trashname):
    simulate(30, 5, 1)
    print trashname, "full", alertApi(host, t, "full", "http").text

def alertApi(host, trashname, endpoint, protocol):
    return requests.post("{}://{}/{}/{}".format(protocol, host, endpoint, trashname))

if __name__ == '__main__':
    host = os.environ['TRASH_HOST']
    trashcans = ["trash" + str(i) for i in range(10)]
    for trash in trashcans:
        print trash, "inserted", alertApi(host, trash, "empty", "http").text

    for trash in trashcans:
        t = Thread(target=simAndAlert, args=(trash,))
        t.start()
