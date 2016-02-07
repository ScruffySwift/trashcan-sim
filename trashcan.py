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

def simAndAlert(trashname, host, lamb, cap, protocol):
    simulate(cap, lamb, 1)
    print trashname, "full", alertApi(host, trashname, "api/full", protocol).text

def simAlertReset(trashname, host, lamb, cap, protocol):
    simulate(cap, lamb, 1)
    print trashname, "full", alertApi(host, trashname, "api/full", protocol).text
    # Sleep for some random amount of time
    sleep_time = np.random.random_integers(cap) + 10
    time.sleep(sleep_time)
    print trashname, "empty", alertApi(host, trashname, "api/empty", "http").text


def alertApi(host, trashname, endpoint, protocol):
    return requests.post("{}://{}/{}/{}".format(protocol, host, endpoint, trashname))

if __name__ == '__main__':
    capacity= os.getenv('TRASH_CAPACITY', 30)
    host = os.getenv('TRASH_HOST', 'localhost:3000')
    ssl = os.getenv('TRASH_SSL', False)

    if ssl:
        protocol = "https"
    else:
        protocol = "http"

    trashcans = ["trash" + str(i) for i in range(10)]
    for trash in trashcans:
        print trash, "inserted", alertApi(host, trash, "api/empty", protocol).text

    # Fill the trashcans
    for trash in trashcans:
        lamb = np.random.random_integers(10)
        t = Thread(target=simAlertReset, args=(trash,host,lamb,capacity,protocol))
        t.start()
