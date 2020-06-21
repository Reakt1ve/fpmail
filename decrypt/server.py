import socket
import subprocess

def server_program():
	host = "127.0.0.1"
	port = 10044

	server_socket = socket.socket()
	server_socket.bind((host, port))

	server_socket.listen(2)
	conn, address = server_socket.accept()

	while True:
        	data = conn.recv(1024).decode()
        	if not data:
			subprocess.call("/home/andrey/decrypt/security.sh")

	conn.close()


if __name__ == '__main__':
    server_program()
