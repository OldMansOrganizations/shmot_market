import psycopg2
import os
from psycopg2 import Error, errors
from dotenv import load_dotenv
import re
from config_db import errors_data, hash_password


class DB:
	# connect to .env file
	load_dotenv()
	
	def __init__(self):
		self.connect = psycopg2.connect
		self.conn = self.connect_to_db()
		self.cursor = self.conn.cursor()
	
	def connect_to_db(self):
		try:
			conn = self.connect(user="postgres",
													database='shmot_online_magazine',
													password=os.getenv('PASSWORD'),
													host="localhost",
													port="5432")
			return conn
		except Error as err:
			print(f'Error to connection --- {err}')
	
	def create_personal_area(self):
		insert_query = f""" INSERT INTO personal_area DEFAULT VALUES RETURNING id_personal_area"""
		self.cursor.execute(insert_query)
		id_personal_area = self.cursor.fetchone()[0]
		return id_personal_area
		
	def create_new_user(self, name, login, password, gmail):
		id_personal_area = self.create_personal_area()
		try:
			# start transaction
			self.conn.autocommit = False
			insert_query = \
				f""" INSERT INTO registered_user
				(name, login, password, gmail, personal_area_id_personal_area)
				VALUES ('{name}', '{login}', '{hash_password(password)}', '{gmail}', '{id_personal_area}')"""
			self.cursor.execute(insert_query)
			# successfully transaction
			self.conn.commit()
		except errors.UniqueViolation as err:
			# error transaction
			self.conn.rollback()
			unique_error = re.search(r'"(\w+)"', str(err.args)).group(1)
			print(errors_data[unique_error])


db = DB()
# db.create_new_user()
