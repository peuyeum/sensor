import serial

from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='root', database='sensorgas')
cursor = cnx.cursor()

skrg = datetime.now()

ser = serial.Serial('COM6', 9600)
temp = ''
while 1:
data=ser.readline().rstrip('\n')
#print data
data=data.strip()
print ('--'+ data)

add_logdata = ("INSERT INTO logdata  "