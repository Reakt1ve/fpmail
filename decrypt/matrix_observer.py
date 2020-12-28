#! /bin/python3
from importlib import util
import asyncio
import aiohttp
import pymysql
from pymysql.cursors import DictCursor
from contextlib import closing
from nio import (AsyncClient, SyncResponse, RoomMessageText)
import os

async_client = AsyncClient(
    "https://citismatrix.zapto.org", "test"
)

def set_dbconnection ():
	connection = pymysql.connect(
					host='localhost',
					user='andrey',
					password='qwerty123',
					db='test',
					charset='utf8mb4',
					cursorclass=DictCursor
                                    )
	return connection

def payload (event, room_id, connection):
	with connection.cursor() as cursor:
		os.system('echo \"' + str(event.body) + '\"')
		os.system('echo \"' + str(event.sender) + '\"')
		query = 'UPDATE users SET sended_notify=\'0\' WHERE room=\"' + str(room_id) + '\"'
		cursor.execute(query)
		connection.commit()

async def tcp_mainSev_client (loop, json_message):
	host = '127.0.0.1'
	port = 10128

	reader, writer = await asyncio.open_connection(host, port, loop=loop)
	writer.write(json_message.encode())
	writer.close()

async def main ():
	response = await async_client.login("qwerty")
	os.system('echo \"' + str(response) + '\"')

	while (True):
		sync_response = await async_client.sync(30000)
		if len(sync_response.rooms.join) > 0:
			joins = sync_response.rooms.join
			for room_id in joins:
				for event in joins[room_id].timeline.events:
					connection = set_dbconnection()
					with closing(connection):
						with connection.cursor() as cursor:
							query = 'SELECT sended_notify FROM users WHERE room=\"' + str(room_id) + '\"'
							cursor.execute(query)
							for record in cursor:
								if isinstance(event, RoomMessageText) and record['sended_notify'] == "1":
									payload(event, room_id, connection)
									#json_message = '{\"body\": \"SIGNAL: user is answer to notify\" \"room_id\": ' + room_id + '}'
									#tcp_mainSev_client(loop, json_message)
	await async_client.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

