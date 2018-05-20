import serial

#from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='root', database='sensor')
cursor = cnx.cursor()

skrg = datetime.now()

ser = serial.Serial('COM3', 9600)