import socket
import config

class Client:
	
	def __init__(self, server_ip):
		self.server_ip = server_ip
		
		self.client = socket.socket()
		
		print ("Connecting to server: ", server_ip, ":", config.server_port)
		self.client.connect((server_ip, config.server_port))
		
	def run(self):
		print("running client...")
		
		#send requests
		
		#receive responses