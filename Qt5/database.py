
# -*- coding: utf-8 -*-



import sqlite3




def create_db(db_name):
	connection = sqlite3.connect(db_name + ".db")
	connection.close()
	print("Database ", db_name + " is created ")