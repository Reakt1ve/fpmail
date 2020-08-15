from matrix_client.api import MatrixHttpApi
from contextlib import closing
import sys
import pymysql

def set_dbconnection ():
        connection = pymysql.connect(
                                        host='localhost',
                                        user='andrey',
                                        password='qwerty123',
                                        db='test',
                                        charset='utf8mb4'
                                    )
        return connection

def update_db():
        connection = set_dbconnection()
        with closing(connection):
                with connection.cursor() as cursor:
                        query = 'UPDATE users SET sended_notify = "1" WHERE room=\"' + '!fiQWALFRGOjvqXQJSK:citis-matrix.ru' + '\"'
			cursor.execute(query)
			connection.commit()

matrix = MatrixHttpApi("https://citismatrix.zapto.org", token="MDAxZGxvY2F0aW9uIGNpdGlzLW1hdHJpeC5ydQowMDEzaWRlbnRpZmllciBrZXkKMDAxMGNpZCBnZW4gPSAxCjAwMjhjaWQgdXNlcl9pZCA9IEB0ZXN0OmNpdGlzLW1hdHJpeC5ydQowMDE2Y2lkIHR5cGUgPSBhY2Nlc3MKMDAyMWNpZCBub25jZSA9IDhtfmJISjp2O3Z0NzdmWVoKMDAyZnNpZ25hdHVyZSDFjdQdLsIYjH4g6an2Jz49nJZkrJbL2D4PJ63NpLEJCAo")
response = matrix.send_message("!fiQWALFRGOjvqXQJSK:citis-matrix.ru", sys.argv[1])
update_db()
