#!/bin/bash

while true; do
    TRASH_CAPACITY=100 TRASH_SSL=true TRASH_HOST=scruffyswift.herokuapp.com ./trashcan.py
    sleep 10
done
