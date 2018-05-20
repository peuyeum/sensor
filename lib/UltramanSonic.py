import serial
import MySQLdb

def readm():
	ArduinoSerial = serial.Serial('COM4', 9600)