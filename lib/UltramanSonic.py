`import serial
import MySQLdb

def readm():
	ArduinoSerial = serial.Serial('COM4', 9600)
	conn=MySQLdb.connect(host='localhost', user='root', passwd='mnabil')
	cursor = conn.cursor()
	try:
		curso.execute('use python_db')
		except MySQLdb.OperationalError, message:
		errorget = '(1094, "Unknown database \'python_db\'")'
		varis = str(message)==errorget