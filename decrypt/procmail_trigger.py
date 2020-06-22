

#sudo echo "signal" | nc -w 1 127.0.0.1 10044

import socket

def client_program():
    host = "127.0.0.1"
    port = 10044

    client_socket = socket.socket()
    client_socket.connect(host, port)

    message = "signal"
    client_socket.send(message.encode())

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
