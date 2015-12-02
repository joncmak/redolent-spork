import socket
import select

import config

class Server:

	def __init__(self, adventure_id):
		self.adventure_id = adventure_id
		
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		
		self.server.bind((config.server_ip, config.server_port))
		self.server.listen(5)
		
		self.connections = [self.server]
		
		serverIP = socket.gethostbyname(socket.gethostname())
		print ('server started on ', serverIP, ':', config.server_port)
		
	def run(self):
		while True:
			(sread, swrite, sexc) = select.select(self.connections, [], [])
			
			for socket in sread:
				if socket == self.server:
					self.accept_new_connection()
				else:
					request = socket.recv(1024)
					
					#process requests
					
					#send response
					
	def accept_new_connection(self):
		new_socket, (host, port) = self.server.accept()
		self.connections.append(new_socket)
		
		