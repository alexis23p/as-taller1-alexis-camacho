
import socket
HOST = 'localhost'
PORT = 9000
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST,PORT))
servidor.listen()

print("elservidor esta a la espera de conexiones...")

cliente, direccion = servidor.accept()
print(f"un cliente {cliente} se conecto desde la direccion{direccion} ")

datos = cliente.recv(1024)
cliente.sendall(b"Hola!" + datos) # ojo! debe ser binario, no cadena
cliente.close()