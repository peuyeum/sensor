import serial

from datetime import date, datetime, timedelta
import mysql.connector

ser = serial.Serial('COM6', 9600)
temp = ''
while 1:
