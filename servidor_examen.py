#Empezamos importando las bibliotecas necesarias
import socket
import threading
import sys
import pickle
import os


class Servidor():#Creamos la clase servidor
	
	def __init__(self, host=socket.gethostname(), port=int(input("Que puerto quiere usar ? "))):#Función que va a pedir al usuario el puerto que quiere usar
		self.clientes = []#Creamos array de clientes
		self.name =[]#Creamos array de nombres
		print('\nSu IP actual es : ',socket.gethostbyname(host))#Muestra la IP actual 
		print('\n\tProceso con PID = ',os.getpid(), '\n\tHilo PRINCIPAL con ID =',threading.currentThread().getName(), '\n\tHilo en modo DAEMON = ', threading.currentThread().isDaemon(), '\n\tTotal Hilos activos en este punto del programa =', threading.active_count())#Muestra los hilos totales del programa
		self.s = socket.socket()
		self.s.bind((str(host), int(port)))#Enlaza el host y el puerto
		self.s.listen(30)
		self.s.setblocking(False)
		

		threading.Thread(target=self.aceptarC, daemon=True).start()
		threading.Thread(target=self.procesarC, daemon=True).start()

		while True:
			msg = input('\n << SALIR = 1 >> \n')#Cerrar el servidor pulsando 1
			if msg == '1':
				print(" **** Me piro vampiro; cierro socket y mato SERVER con PID = ", os.getpid())#Mensaje que le va a salir al usuario cuando cierre el servidor
				self.s.close()
				sys.exit()
			else: pass

	def aceptarC(self):#Función que sirve para aceptar el mensaje enviado por el cliente
		print('\nHilo ACEPTAR con ID =',threading.currentThread().getName(), '\n\tHilo en modo DAEMON = ', threading.currentThread().isDaemon(),'\n\tPertenece al PROCESO con PID', os.getpid(), "\n\tHilos activos TOTALES ", threading.active_count())#Muestra los hilos totales
		
		while True:
			try:
				conn, addr = self.s.accept()
				print(f"\nConexion aceptada via {addr}\n")#Conexion aceptada
				conn.setblocking(False)
				self.clientes.append(conn)
				data = conn.recv(32).decode()
				if data:#Creamos un if para ver si el nickname es aceptado o no por el servidor
					name = data
					print("Nickname aceptado" , name)
					self.name.append(name)
			except: pass

	def procesarC(self):#Creamos la función procesar los mensajes que va recibiendo del cliente
		print('\nHilo PROCESAR con ID =',threading.currentThread().getName(), '\n\tHilo en modo DAEMON = ', threading.currentThread().isDaemon(),'\n\tPertenece al PROCESO con PID', os.getpid(), "\n\tHilos activos TOTALES ", threading.active_count())#Ver hilos totales
		while True:
			if len(self.clientes) > 0:
				for c in self.clientes:
					try:
						data = c.recv(32)
						if data: self.broadcast(data,c)
						with open('ue22166872AI1.txt', 'a') as f:#Creamos el txt para ir añadiendo todos los mensajes que vaya recibiendo el servidor
							f.write(pickle.loads(data) + '\n')#Los va poniendo uno detrás de otro
					except: pass

	def broadcast(self, msg, cliente):#Función para ver los clientes conectados e imprimir sus nicknames
		for c in self.clientes:
			print("Clientes conectados Right now = ", len(self.clientes), ' ',self.name, '\tMensaje de: ', pickle.loads(msg))#Imprime el nickname del cliente que ha escrito el mensaje
			try:
				if c != cliente: 
					
					c.send(msg)
			except: self.clientes.remove(c)

arrancar = Servidor() #Función para arrancar el servidor