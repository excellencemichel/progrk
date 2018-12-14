#! /usr/bin/python3
# -*- coding: utf-8 -*-

"""
Fichier pour les données
"""


import psycopg2
from pprint import  pprint




class Database:

	def __init__(self):
		pass



	def connexion_database(self, dbname, user, host, password, port):
		# self.dbname =dbname
		# self.user = user
		# self.host = host
		# self.password = password
		# self.port = port

		try:
			conn = psycopg2.connect("dbname= '{dbname}' user = '{user}' host = '{host}' password ='{password}' port = '{port}'".format(dbname=dbname, user=user, host=host, password =password, port =port))
			self.cursor = conn.cursor()

		
		except psycopg2.OperationalError as e :
			raise pprint("Cant connect dadabase because {}".format(e))
		except psycopg2.ProgrammingError as e:
			pprint("Error de code because: {}".format(e))



	def crate_tabe_db_inscription(self, table_name):

		create_table_commande = """ CREATE TABLE {table_name} ( id serial PRIMARY KEY, prenom varchar(250), nom varchar(250) NOT NULL, username varchar(250) UNIQUE NOT NULL, password varchar(250) NOT NULL ) """
		try:
			self.cursor.execute(create_table_commande)


		except psycopg2.ProgrammingError:
			pprint("Une erreur SQL")

		except Error:
			pprint("Une erreur python")


	def insert_data_inscription(prenom, nom, username, password):
		insert_data_commande = (""" INSERT INTO {table_name} (prenom, nom, username, password) VALUES( "{prenom}" "{nom}" "{username}" "{password}" )""".format(prenom=prenom, nom=nom, username=username, password=password))

		try:
			self.cursor.execute(insert_data_commande)
			pprint("Success insertion")

		except psycopg2.ProgrammingError:
			pprint("Une erreur SQL")
		except Error:
			pprint("Error python")

