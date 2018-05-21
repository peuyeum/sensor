import serial
import MySQLdb

def readm():
	ArduinoSerial = serial.Serial('COM4', 9600)
	conn=MySQLdb.connect(host='localhost', user='root', passwd='mnabil')
	cursor = conn.cursor()