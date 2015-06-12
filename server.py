import sqlite3
import serial
import datetime

# Connecting to database
con=sqlite3.connect('server.db')

if con:
	print 'Connected to Data base succesfully'
else :
	print 'failed Database connection cahnge permission to read and write'
try: con.execute(''' CREATE TABLE Datas
	        (SNO INTEGER PRIMARY KEY AUTOINCREMENT,
	         TIME TEXT,
	         TEMP INTEGER,
	         HUMID INTEGER,
	         MOIST INTEGER,
	         RTIME INTEGER
	        	);''')		
finally:
	print "Table already exist"
port=serial.Serial("/dev/ttyACM0",9600)
if port:
	print "opened port succesfully"
	while 1:
		trigtim=datetime.datetime.now().strftime("%H")
		final=con.execute(''' SELECT COUNT (*) FROM Datas;''')
		k=con.execute(''' SELECT RTIME FROM Datas WHERE SNO=final ''')
		
		if trigtim==7 or trigtim==13 or trigtim==18 :
			port.write(k) #k is the time which motor should run on the system

			
		print 'waiting...'
		rcv=port.readline()
		rcv=rcv.strip()
		print "recieved data :",rcv
		if len(rcv)>0:
			temptr=int(rcv[1:2])
			humidt=int(rcv[3:4])
			moistr=int(rcv[5:6])
			rtime=datetime.datetime.now()
			con.execute('''' INSERT INTO Datas
				(TIME,TEMP,HUMID,MOIST)
				VALUES(rtime,temptr,humidt,moistr)
					)
				''');
			con.commit()
con.close()
port.close()			

		
			
		
	
