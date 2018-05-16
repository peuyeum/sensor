import serial
import MySQLdb

def readm(hos, use, pas, por, dbname):
	ArduinoSerial = serial.Serial('COM4', 9600)
	conn=MySQLdb.connect(host='localhost', user='root', passwd='mnabil')
	cursor = conn.cursor()
	try:
		curso.execute('use python_db')
		except MySQLdb.OperationalError, message:
		errorget = '(1094, "Unknown database \'python_db\'")'
		varis = str(message)==errorget
		print errorget
		print str(message)
		if varis:
			cursor.execute('create database python_db')
		while True:
			readed = str(ArduinoSerial.readline())
			readlen = len(readed)-2
			cursor.execute("INSERT INTO py_test(jarak) VALUES(concat(%s,'cm'))", [readed[0:readlen]])
			conn.commit()
			print ("INSERT INTO py_test(jarak) VALUES(concat(%s,'cm'))", [readed[0:readlen]])

def posInput(hos, use, pas, por, dbname):
	ArduinoSerial = serial.Serial(por, 9600)
	conn=psycopg2.connect("dbname='"+dbname+"' user='"+use+"' password='"+pas+"'")			