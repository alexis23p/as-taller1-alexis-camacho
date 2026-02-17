
import socket
import threading

HOST = '0.0.0.0'
PORT = 5000

store = {}
lock = threading.Lock()


def handle_client(conn, addr):
	with conn:
		conn.sendall(b"Servidor KV listo. Comandos: SET GET DEL KEYS QUIT\n")
		buffer = b""
		while True:
			data = conn.recv(1024)
			if not data:
				break
			buffer += data
			while b"\n" in buffer:
				line, buffer = buffer.split(b"\n", 1)
				cmd = line.decode('utf-8', errors='ignore').strip()
				if not cmd:
					continue
				parts = cmd.split(' ', 2)
				action = parts[0].upper()
				if action == 'SET' and len(parts) >= 3:
					key = parts[1]
					value = parts[2]
					with lock:
						store[key] = value
					conn.sendall(b"OK\n")
				elif action == 'GET' and len(parts) >= 2:
					key = parts[1]
					with lock:
						val = store.get(key)
					if val is None:
						conn.sendall(b"NOT_FOUND\n")
					else:
						conn.sendall((val + "\n").encode())
				elif action in ('DEL', 'DELETE') and len(parts) >= 2:
					key = parts[1]
					with lock:
						existed = store.pop(key, None) is not None
					conn.sendall(b"DELETED\n" if existed else b"NOT_FOUND\n")
				elif action == 'KEYS':
					with lock:
						keys = ' '.join(store.keys())
					conn.sendall((keys + "\n").encode())
				elif action == 'QUIT':
					conn.sendall(b"BYE\n")
					return
				else:
					conn.sendall(b"ERR Unknown command\n")


def main():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind((HOST, PORT))
	sock.listen(5)
	print(f"Servidor KV escuchando en {HOST}:{PORT}")
	try:
		while True:
			conn, addr = sock.accept()
			print(f"Conexión desde {addr}")
			t = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
			t.start()
	except KeyboardInterrupt:
		print('\nServidor detenido por teclado')
	finally:
		sock.close()


if __name__ == '__main__':
	main()



