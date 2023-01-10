#Empezamos importando las bibliotecas necesarias
import threading
import sys
import socket
import pickle
import os

class Cliente():
	
	def __init__(self, name=input("Intoduzca el nickname:  "), host=input("Intoduzca la IP del servidor ?  "), port=int(input("Intoduzca el PUERTO del servidor ?  "))): #Función que pide al cliente el nickname(correo de la universidad) y el puerto
		self.s = socket.socket()
		self.s.connect((host, int(port)))#Conecta el host con el puerto

		self.name=name
		self.s.send(name.encode())#Pasamos el nickname al servidor para que tenga el dato y poder manejarlo después
		print('\n\tProceso con PID = ',os.getpid(), '\n\tHilo PRINCIPAL con ID =',threading.currentThread().getName(), '\n\tHilo en modo DAEMON = ', threading.currentThread().isDaemon(),'\n\tTotal Hilos activos en este punto del programa =', threading.active_count())#Imprime los hilos que se van a utilizar
		threading.Thread(target=self.recibir, daemon=True).start()

		while True:
			msg = input('\n Nickname: ' + self.name + '\tEscriba texto ?   ** Enviar = ENTER   ** Salir Chat = 1 \n')#Menú que le va a salir al cliente en el cual va a aprecer el nickname y una opción para poder enviar un mensaje. Para salir del menú tendra que pulsar 1.
			if msg != '1' : self.enviar(msg)#Si el ususario escribe otra cosa que no es 1 envía el mensaje
			else:
				print(" **** Me piro vampiro; cierro socket y mato al CLIENTE con PID = ", os.getpid())#Mensaje que le va a salir cuando pulse 1 y cierre el cliente
				self.s.close()
				sys.exit()

	def recibir(self):#Función para poder ver los hilos que van a salir y los que están activos en este momento
		print('\nHilo RECIBIR con ID =',threading.currentThread().getName(), '\n\tPertenece al PROCESO con PID', os.getpid(), "\n\tHilos activos TOTALES ", threading.active_count())
		while True:
			try:
				data = self.s.recv(32)
				if data: print(pickle.loads(data))
			except: pass

	def enviar(self, msg):#Función que sirve para que aparezca el nickname al enviar el mensaje
		mensaje = f"{self.name}: {msg}"
		self.s.send(pickle.dumps(mensaje))

arrancar = Cliente()#Función para arrancar el cliente