#!/usr/bin/python

import socket

def client_program():
    host = "127.0.0.1"
    port = 10128

    client_socket = socket.socket()
    client_socket.connect((host, port))

    json_message = 'SIGNAL'
    client_socket.send(json_message.encode())

    client_socket.close()

if __name__ == '__main__':
    client_program()
