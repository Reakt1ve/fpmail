#!/usr/bin/python

#################################################### SYNC SERVER #######################################################################

import socket
import subprocess

def server_program():
	host = "0.0.0.0"
	port = 10128

	server_socket = socket.socket()
	server_socket.bind((host, port))

	server_socket.listen(5)

	while True:
		conn, address = server_socket.accept()
        	data = conn.recv(1024).decode()
        	if not data:
			continue

		subprocess.call("/home/alexeysenu/informator/decrypt/security.sh")

	conn.close()


if __name__ == '__main__':
    server_program()

###################################################### ASYNC SERVER ###################################################################3

#import asyncio
#import aiohttp
#import subprocess
#import sys
#import json
#from client import matrix_cli, asterisk_cli, email_cli

#def set_dbconnection ():
#        connection = pymysql.connect(
#                                        host='localhost',
#                                        user='andrey',
#                                        password='qwerty123',
#                                        db='test',
#                                        charset='utf8mb4'
#                                    )
#        return connection
#
#def update_db (value, room_id):
#        connection = set_dbconnection()
#        with closing(connection):
#                with connection.cursor() as cursor:
#                        query = 'UPDATE users SET sended_notify =\"' + str(value) + '\" WHERE room=\"' + str(room_id) + '\"'
#                        cursor.execute(query)
#                        connection.commit()
#
#async def matrix_connection (type, text):
#	matrix = MatrixHttpApi("https://citismatrix.zapto.org", token="MDAxZGxvY2F0aW9uIGNpdGlzLW1hdHJpeC5ydQowMDEzaWRlbnRpZmllciBrZXkKMDAxMGNpZCBnZW4gPSAxCjAwMjhjaWQgdXNlcl9pZCA9IEB0ZXN0OmNpdGlzLW1hdHJpeC5ydQowMDE2Y2lkIHR5cGUgPSBhY2Nlc3MKMDAyMWNpZCBub25jZSA9IEF3YXE9UGcmNjdVbzE1bioKMDAyZnNpZ25hdHVyZSAQdp0_lujFeDL5As5DRxsrzX1C0vbXhgun7SrhmG0RhQo")
#	matrix.send_message("!fiQWALFRGOjvqXQJSK:citis-matrix.ru", text)
#
#	if type == "reply":
#		update_db(1, room_id)
#		return True
#	elif type  == "noreply":
#		return True
#	else:
#		print("ERROR: bad matrix connection type")
#		return False
#
#async def run_coordinator (reader, writer):
	# Init additional modules
#	if not init_modules():
#		return 1
#
#	while True:
#		data = await reader.read(100)
#		message = data.decode()
#		json_message = json.loads(message)
#
		#handler for different modules
#		if 'Fetchmail' in json_message['service']:
#			proc_result = subprocess.run("/home/andrey/decrypt/security.sh")
#			if not proc_result.returncode:
#				await client_coordinator(message, "SPR")
#		elif 'SPR' in json_message['service']:
#			if 'Matrix' in json_message['channel']:
#				await client_coordinator(json_message, "MATRIX_CLI")
#			elif 'Asterisk' in json_message['channel']:
#				await client_coordinator(json_message, "ASTERISK_CLI")
#			elif 'Email' in json_message['channel']:
#				await client_coordinator(json_message, "EMAIL")
#			else
#				print("ERROR: bad messanger type")
#		elif 'Matrix_client' in json_message['service']:
#			await client_coordinator(json_message, "SPR")
#		elif 'Asterisk' in json_message['service']:
#			await client_coordinator(json_message, "SPR")
#		else
#			print("ERROR: bad signal")

#async def client_coordinator (json_object, service):
#	if "MATRIX_CLI" in service:
#		reader, writer = await asyncio.open_connection(HOST, MATRIX_CLI_PORT, loop=loop)
#	elif "ASTERISK_CLI" in service:
#		reader, writer = await asyncio.open_connection(HOST, ASTERISK_CLI_PORT, loop=loop)
#	elif "SPR" in service:
#		reader, writer = await asyncio.open_connection(HOST, SPR_PORT, loop=loop)
#	elif "EMAIL" in service:
#		proc_result = subprocess.run("/home/andrey/decrypt/send_mail.py", json_object)
#		if not proc_result.returncode;
#			return 0
#		else
#			return -1
#	else
#		print("ERROR: bad service")
#		return -1
#
#	return 0
#
#def init_modules ():
#	if start_MatrixClientService():
#               return -1
#
#        if start_AsteriskClientService():
#                return -1
#
#def start_MatrixClientService ():
#	subprocess.Popen(['service', 'matrix_client', 'start'],
#			stdout=subprocess.PIPE,
#			stderr=subprocess.STDOUT)
#
#	if stderr == 1:
#		return -1
#
#def start_AsteriskClientService ():
#	subprocess.Popen(['service', 'asterisk_client', 'start'],
#			stdout=subprocess.PIPE,
#			stderr=subprocess.STDOUT)
#
#	if stderr == 1:
#		return -1
#
#if __name__ == "__main__":
#	# Init event loop
#	loop = asyncio.get_event_loop()
#
#	# Run app in loop
#	server_handler = asyncio.start_server(run_coordinator, HOST, PORT, loop=loop)
#	server = loop.run_until_complete(server_handler)
#
#	try:
#		loop.run_forever()
#	except KeyboardInterrupt:
#		pass
#
#	# Close event loop
#	loop.close()

