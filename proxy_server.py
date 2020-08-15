import	socket
import	subprocess

def server_program():
	host = "172.27.200.2"
	port = 40120

	server_socket =	socket.socket()
	server_socket.bind((host, port))

	server_socket.listen(2)

	while True:
		conn, address = server_socket.accept()
		data = conn.recv(1024).decode()
		if not data:
			continue

		subprocess.call(["/home/alexeysenu/informator/encrypt/encrypt.sh", str(data)])        
		
	conn.close()


if __name__ == '__main__':
    server_program()

