import socket
import  threading

HOST ='localhost'
PORT = 9000

def recibir_mensajes():
    while  True:
        mensaje = cliente.recv(1024).decode()
        print(mensaje)    

nombre = input("Cual es tu nombre:")
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
cliente.connect((HOST, PORT))
cliente.sendall(nombre.encode())

hilo_recibir = threading.Thread(tarjet=recibir_mensajes)
hilo_recibir.start()

while True:
    mensaje = input("Ingrese un mensaje: ")
    cliente.sendall(mensaje.encode())
    
cliente.close()


