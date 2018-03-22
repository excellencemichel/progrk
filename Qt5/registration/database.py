#! /usr/bin/python3
#-*-coding:utf-8-*-



import psycopg2
from pprint import  pprint



def createtbale():

	try:

		connection = psycopg2.connect(
										"dbname = 'formation' user = 'michel' host = 'localhost' password = 'SaintMichel' port ='5432' "
									 )

		connection.autocommit = True

		cursor = connection.cursor()

	except:
		pprint("Cant connect on database !")



	create_table_command = "CREATE TABLE users( id serial PRIMARY KEY, username varchar(250) NOT NULL, email varchar(250) NOT NULL , password varchar NOT NULL )"

	cursor.execute(create_table_command)

	insert_command = "INSERT INTO users(username, email, password) VALUES('Michel', 'bnvnmmnl@gmail.com', 'Michel123')"
	print(type(insert_command))
	cursor.execute(insert_command)


	select_command = " SELECT * FROM users"

	cursor.execute(select_command)
	result = cursor.fetchall()


	for data in result:
		pprint("Username : {}".format(data))




if __name__ == '__main__':
	createtbale()