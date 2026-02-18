#servidor.py
import socket
import threading

HOST = 'localhost'
PORT = 9000

clientes = []

def atender_cliente(cliente_skt,cliente_nombre):

    while True:
        try:
            mensaje=cliente_skt.recv(1024)
            if not mensaje:
                break

            print(f" {cliente_nombre}:  {mensaje.decode()}")
            broacast(mensaje.decode() ,cliente_skt)
        except ConnectionResetError:
            clientes.remove(cliente_skt)
            cliente_skt.close()
            break

def broacast(mensaje,emisor):
    for cliente in clientes:
        if cliente != emisor:
            cliente.sendall(mensaje.encode())

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST,PORT))
servidor.listen()
print("el servidor  'chat' esta a la esperando  de conexiones...")
while True:

    cliente, direccion = servidor.accept()
    print(f"un clienteconectado desde la IP {direccion} ")
    nombre_cliente=cliente.recv(1024).decode()
    clientes.append(cliente)
    broacast(f"{nombre_cliente} se ha unido al chat", cliente)
    hilo_cliente  = threading.Thread(target=atender_cliente,args=(cliente,nombre_cliente))
    hilo_cliente.start()