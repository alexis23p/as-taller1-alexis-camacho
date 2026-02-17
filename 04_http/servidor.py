import socket
import http.server

HOST = 'localhost'
PORT = 9000

class ServidorHTTP(http.server.SimpleHTTPRequestHandler):
    pass

servidor = http.server.HTTPServer((HOST , PORT) , ServidorHTTP)
servidor.serve_forever()