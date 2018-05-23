import serial

#from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='root', database='sensor')
cursor = cnx.cursor()

skrg = datetime.now()

ser = serial.Serial('COM3', 9600)
temp = ''
while 1:
	data=ser.readline().rstrip('\n')
	#print data
	data=data.strip()
	print ('--'+ data)
	
	add_logdata = ("INSERT INTO sensor_warna "
               "(tgl, serial) "
               "VALUES (%s, %s)")

	dataB = (skrg, data)

	# Insert new employee
	cursor.execute(add_logdata, dataB)

	# Make sure data is committed to the database
	cnx.commit()
	
cursor.close()
cnx.close()
