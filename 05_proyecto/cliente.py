
import socket
import sys

DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 5000


def main(host=DEFAULT_HOST, port=DEFAULT_PORT):
	try:
		with socket.create_connection((host, port)) as s:
			greeting = s.recv(1024).decode().strip()
			if greeting:
				print(greeting)
			while True:
				try:
					cmd = input('> ').strip()
				except EOFError:
					print()
					break
				if not cmd:
					continue
				s.sendall((cmd + '\n').encode())
				data = s.recv(4096)
				if not data:
					print('Conexión cerrada por el servidor')
					break
				print(data.decode().strip())
				if cmd.split()[0].upper() == 'QUIT':
					break
	except ConnectionRefusedError:
		print(f'No se pudo conectar a {host}:{port}')
	except KeyboardInterrupt:
		print('\nInterrumpido por usuario')


if __name__ == '__main__':
	h = DEFAULT_HOST
	p = DEFAULT_PORT
	if len(sys.argv) >= 2:
		h = sys.argv[1]
	if len(sys.argv) >= 3:
		try:
			p = int(sys.argv[2])
		except ValueError:
			pass
	main(h, p)



