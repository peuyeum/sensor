import serial
import MySQLdb

def test()
	ArduinoSerial = serial.Serial('com4', 9600)
	conn = MySQLdb.connect('localhost', 'root', '', 'arduino_db')
	cursor = conn.cursor()