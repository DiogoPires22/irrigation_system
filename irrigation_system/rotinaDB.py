import serial,sqlite3, datetime, json,sys, os

#atribui a conexao serial
aberto=True
ser=serial.Serial('/dev/ttyACM0',9600)


import numbers

while 1:
  
    try:
		#abre uma conexao com o banco da aplicacao
		conn=sqlite3.connect('db.sqlite3')
		#atribui um cursor a variavel c
		c=conn.cursor()
		
		#verifica se o sistema esta ativado
		c.execute("SELECT status FROM irrigation_status")
		rows=c.fetchall()
		status=rows[0][0]
		#se estiver ligado(status=1) faremos a comunicacao serial, e iremos inserir uma tupla com o valor do sensor e o horario da medicao
		if status==1:
			ser.open()
			aberto=True
			#informa o arduino q o sistema esta ligado
			ser.write('1')
			
			#atribui a variavel o retorno do arduino
			moisture=ser.readline()

			#converte o retorno em um json object
			json_object=json.loads(moisture)
			#informa o valor do sensor no terminal
			                 
			print(json_object["moisture"])
			#faz a insercao do valor no banco
			c.execute('INSERT INTO irrigation_soilmoisturecontrol (moisture,date) vALUES (?,?)',(json_object["moisture"],datetime.datetime.now()))
			#comita a insercao
			conn.commit()
			#fecha a conexao com o banco
			conn.close()
		else:
			#se estiver com status 0 informamos ao arduino q o sistema esta desativado
			if aberto:
				ser.close()
				aberto=False	
			print("sistema desligado")
		
    except Exception as ex:
		exc_type,exc_value,exc_traceback=sys.exc_info()
		print(ex)
		print exc_traceback.tb_lineno
	
    #time.sleep(5)
