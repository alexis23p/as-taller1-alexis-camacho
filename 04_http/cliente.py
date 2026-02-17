import socket
import http.client

HOST = 'localhost'
PORT = 9000

cliente = http.client.HTTPConnection(HOST, PORT)

cliente.request("GET",  "/")

repuesta = cliente.getresponse()
datos = repuesta.read().decode()
print(datos)
cliente.close()