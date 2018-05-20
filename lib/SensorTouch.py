import serial
import MySQLdb

def test()
	ArduinoSerial = serial.Serial('com4', 9600)
	conn = MySQLdb.connect('localhost', 'root', '', 'arduino_db')
	cursor = conn.cursor()
	try:
		cursor.execute('use arduino_db')
	except MySQLdb.OperationalError, message:
		errorget = '(1049, "Unknown database \'arduino_db\'")'
		varis = str(message)==errorget    
		if varis:
			cursor.execute('create database arduino_db')
			cursor.execute('use arduino_db')
			cursor.execute('CREATE TABLE hasil_serial(hasil_uji INT(10))')
		while True:
		readed = str(ArduinoSerial.readline())