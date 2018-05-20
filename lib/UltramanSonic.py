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
	conn=psycopg2.connect("dbname='"+dbname+"' user='"+use+"' password='"+pas+"'")cursor = conn.cursor()
	try:
		result = cursor.execute("select * from py_ultraman_sonic")		
		conn.rollback()
		errorget = "relation \"py_ultraman_sonic\" does not exist\nLINE 1: select * from bar"
		varis = str(message)[0:43]==errorget[0:43]
		print errorget[0:43]
		print str(message)[0:43]
		print varis		
		if varis:
			cursor.execute('CREATE TABLE py_ultraman_sonic(id SERIAL, jarak VARCHAR(20) NOT NULL)')
	while True:
		readed = str(ArduinoSerial.readline())
		readlen = len(readed)-2		