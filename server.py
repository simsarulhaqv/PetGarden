import sqlite3
import serial
import datetime

con=sqlite3.connect('PetGarden/db.sqlite3')
if con:
	print 'Connected to Data base succesfully'
else :
	print 'failed Database connection cahnge permission to read and write'
#if con.execute(''' CREATE TABLE Datas
#	        (SNO INTEGER PRIMARY KEY AUTOINCREMENT,
#	         CTIMES TEXT,
#	         TEMP INTEGER,
#	         HUMID INTEGER,
#	         MOIST INTEGER,
#	         LIGHT INTEGER,
#	         SURFTEMP INTEGER,
#	         LEAFMOIST INTEGER,
#	         RTIME INTEGER
#	        	);'''):
#	        	print "Table created succesfully"		
#else:
#	print "Table already exist"
	
#port=serial.Serial("/dev/ttyACM0",9600)
#if port:
#	print "opened port succesfully"
#	while 1:
#		k=con.execute(''' SELECT RTIME FROM Datas WHERE SNO=(SELECT MAX(SNO)  FROM Datas)''')
#		
#		if(k):
#			snd="x" + str (k) + "y"  #this is the recieving format kp want
#			port.write(snd)
#
#
#		print 'waiting...'
#		rcv=port.readline()
#		rcv=rcv.strip()
#		print "recieved data :",rcv
#		if len(rcv)>0:
#			temptr=int(rcv[0:2])
#			humidt=int(rcv[2:4])
#			moistr=int(rcv[4:6])
#			lite=int(rcv[6:8]) 
#			srft=int(rcv[8:10]) #surface temp
#			lifm=int(rcv[10:12])   #leaf moisture
#
#			rtime=datetime.datetime.now()
con.execute(''' INSERT INTO plant_details_plantdetailpost
		(CTIMES,TEMP,HUMID,MOIST,LIGHT,SURFTEMP,LEAFMOIST,RTIME)
		VALUES (34,23,34,45,65,43,23,54);''')
con.commit()
con.close()
#port.close()			

		
			
		
	
