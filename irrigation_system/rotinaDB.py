import serial,sqlite3, datetime, json

ser = serial.Serial('/dev/ttyACM0',9600)


import numbers

while 1:
    moisture=ser.readline()
    #print(moisture)
    
    try:
		conn=sqlite3.connect('db.sqlite3')
		c=conn.cursor()
		json_object=json.loads(moisture)
		print(json_object["moisture"])
		c.execute('INSERT INTO irrigation_soilmoisturecontrol (moisture,date) vALUES (?,?)',(json_object["moisture"],datetime.datetime.now()))
		conn.commit()
		conn.close()
    except Exception as ex:
		print ex
   
    #time.sleep(5)
