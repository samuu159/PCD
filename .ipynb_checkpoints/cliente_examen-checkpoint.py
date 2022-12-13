{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c901af7a-2ae6-461c-ab95-d7ea8c6616bc",
   "metadata": {},
   "outputs": [],
   "source": [
    "import threading\n",
    "import sys\n",
    "import socket\n",
    "import pickle\n",
    "import os\n",
    "\n",
    "class Cliente():\n",
    "\t\n",
    "\tdef __init__(self, name=input(\"Intoduzca el nickname:  \"), host=input(\"Intoduzca la IP del servidor ?  \"), port=int(input(\"Intoduzca el PUERTO del servidor ?  \"))): #Función que pide al cliente el nickname(correo de la universidad) y el puerto\n",
    "\t\tself.s = socket.socket()\n",
    "\t\tself.s.connect((host, int(port)))#Conecta el host con el puerto\n",
    "\n",
    "\t\tself.name=name\n",
    "\t\tself.s.send(name.encode())#Pasamos el nickname al servidor para que tenga el dato y poder manejarlo después\n",
    "\t\tprint('\\n\\tProceso con PID = ',os.getpid(), '\\n\\tHilo PRINCIPAL con ID =',threading.currentThread().getName(), '\\n\\tHilo en modo DAEMON = ', threading.currentThread().isDaemon(),'\\n\\tTotal Hilos activos en este punto del programa =', threading.active_count())#Imprime los hilos que se van a utilizar\n",
    "\t\tthreading.Thread(target=self.recibir, daemon=True).start()\n",
    "\n",
    "\t\twhile True:\n",
    "\t\t\tmsg = input('\\n Nickname: ' + self.name + '\\tEscriba texto ?   ** Enviar = ENTER   ** Salir Chat = 1 \\n')#Menú que le va a salir al cliente en el cual va a aprecer el nickname y una opción para poder enviar un mensaje. Para salir del menú tendra que pulsar 1.\n",
    "\t\t\tif msg != '1' : self.enviar(msg)#Si el ususario escribe otra cosa que no es 1 envía el mensaje\n",
    "\t\t\telse:\n",
    "\t\t\t\tprint(\" **** Me piro vampiro; cierro socket y mato al CLIENTE con PID = \", os.getpid())#Mensaje que le va a salir cuando pulse 1 y cierre el cliente\n",
    "\t\t\t\tself.s.close()\n",
    "\t\t\t\tsys.exit()\n",
    "\n",
    "\tdef recibir(self):#Función para poder ver los hilos que van a salir y los que están activos en este momento\n",
    "\t\tprint('\\nHilo RECIBIR con ID =',threading.currentThread().getName(), '\\n\\tPertenece al PROCESO con PID', os.getpid(), \"\\n\\tHilos activos TOTALES \", threading.active_count())\n",
    "\t\twhile True:\n",
    "\t\t\ttry:\n",
    "\t\t\t\tdata = self.s.recv(32)\n",
    "\t\t\t\tif data: print(pickle.loads(data))\n",
    "\t\t\texcept: pass\n",
    "\n",
    "\tdef enviar(self, msg):#Función que sirve para que aparezca el nickname al enviar el mensaje\n",
    "\t\tmensaje = f\"{self.name}: {msg}\"\n",
    "\t\tself.s.send(pickle.dumps(mensaje))\n",
    "\n",
    "arrancar = Cliente()#Función para arrancar el cliente"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
