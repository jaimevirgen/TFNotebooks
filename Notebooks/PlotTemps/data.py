#!/usr/bin/python

import csv
import datetime
import os
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

now = datetime.datetime.now()
dayStr = now.strftime("%Y%m%d")  # 20180619
datapath = '/home/pi/Desktop/Data/'
fullfilepath = datapath + dayStr + '.csv'

if not os.path.exists(datapath):
    os.makedirs(datapath)

# GET TEMP/PRESSURE/HUMIDITY DATA READINGS

Ctemp = sense.get_temperature()
humidity = sense.get_humidity()
pressure = sense.get_pressure()

# CALIBRATION ADJUSTMENT

Ftemp = (9.0 / 5.0 * Ctemp + 32) - 10.2
humidity = humidity + 9.0

# Write CSV header

if not os.path.exists(fullfilepath):
    with open(fullfilepath, 'a') as newFile:
        newFileWriter = csv.writer(newFile)
        newFileWriter.writerow(['datetime', 'Temperature-Internal', 'Humidity', 'Pressure'])

# Write Data Record

with open(fullfilepath, 'a') as newFile:
    newFileWriter = csv.writer(newFile)
    newFileWriter.writerow([now, Ftemp, humidity, pressure])


