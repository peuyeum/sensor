import serial
import MySQLdb
import psycopg2

def myInput(hos, use, pas, por, dbname):
	ArduinoSerial = serial.Serial(por, 9600)
	conn=MySQLdb.connect(hos, use, pas, dbname)
	cursor = conn.cursor()	
	try:
		result = cursor.execute("select * from py_ultraman_sonic")
	except MySQLdb.ProgrammingError, message:
		errorget = "(1146, \"Table '"+dbname+".py_ultraman_sonic' doesn't exist\")"
		varis = str(message)==errorget
		print errorget
		print str(message)
		if varis:			
			cursor.execute('CREATE TABLE py_ultraman_sonic(id INT(3) NOT NULL PRIMARY KEY AUTO_INCREMENT, jarak VARCHAR(20) NOT NULL,waktu TIMESTAMP DEFAULT CURRENT_TIMESTAMP)')
	while True:
		readed = str(ArduinoSerial.readline())
		readlen = len(readed)-2		
		cursor.execute("INSERT INTO py_ultraman_sonic(jarak) VALUES(concat(%s,'cm'))", [readed[0:readlen]])
		conn.commit()
		print ("INSERT INTO py_ultraman_sonic(jarak) VALUES(concat(%s,'cm'))", [readed[0:readlen]])

def posInput(hos, use, pas, por, dbname):
	ArduinoSerial = serial.Serial(por, 9600)
	conn=psycopg2.connect("dbname='"+dbname+"' user='"+use+"' password='"+pas+"'")
	cursor = conn.cursor()
	try:
		result = cursor.execute("select * from py_ultraman_sonic")
	except psycopg2.ProgrammingError, message:
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
		cursor.execute("INSERT INTO py_ultraman_sonic(jarak) VALUES(concat(%s,'cm'))", [readed[0:readlen]])
		conn.commit()
		print ("INSERT INTO py_ultraman_sonic(jarak) VALUES(concat(%s,'cm'))", [readed[0:readlen]])	

		
#myInput("localhost", "root", "mnabil", "COM4", "python_db_ultraman")
#posInput("localhost", "postgres", "mnabil17", "COM4", "python_db")