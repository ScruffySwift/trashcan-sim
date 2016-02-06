#!/usr/bin/env python

import numpy as np
import time

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
        print val
        count += val
        time.sleep(sleep)
    return True

if __name__ == '__main__':
    print simulate(30, 5, 1)
