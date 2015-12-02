import sys
from server import Server
from client import Client

ADVENTURES = ["demo"]

if __name__ == '__main__':
	print("Welcome\n")
	print("Main Menu:\n1) Host Game\n2) Join Game\n3) Exit\n")
	
	invalid_command = True
	
	while(invalid_command):
		menu_command = input("Enter command number:")
		invalid_command = False

		if(menu_command == "1"):
			print("The currently available adventures are:")
			print(ADVENTURES)
			print("")
			invalid_adventure = True
			
			while(invalid_adventure):
				mission_id = input("Select the adventure to play:")
				invalid_adventure = False
				
				if(mission_id in ADVENTURES):
					print("Starting Server...")
					server = Server(mission_id)
					server.run()
				else:
					print("Invalid Adventure. Please try again.")
					invalid_adventure = True
				
		elif(menu_command == "2"):
			server_ip = input("Enter the IP Address of the server to connect to:")
			client = Client(server_ip)
		elif(menu_command == "3"):
			print("Exiting...\nGoodbye")
			sys.exit()
		else:
			print("Invalid Action. Please try again.")
			invalid_command = True