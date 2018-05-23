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
			"(kadar_gas,Tanggal) "
			"VALUES (%s, %s)")
	
	dataB = (data, skrg)

	# Insert new employee
	cursor.execute(add_logdata, dataB)

	# Make sure data is committed to the database
	cnx.commit()
	
cursor.close()
cnx.close()
