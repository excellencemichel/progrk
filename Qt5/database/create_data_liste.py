#! /usr/bin/python
#-*-coding:utf-8-*-



import sys
import psycopg2
from pprint import  pprint





class Create:

	"""
	Classe pour la connexion à la base de données
	Le problème majeur est comment initier la creation d'une table dans la base de données et
	garder la même instance pour l'insertion des données dans cettes table
	par celà il y a rique que dès la création d'un objet de la classe qu'il ait crétion directement
	d'une table chose qui n'est pas bonne bonne car la classe n'as pas pour simple rôle de créer
	des tables, on peut aussi inserrer des données et les recupérer voir aussi les supprimer si
	ça simpose
	celà dit il faut alors qu'a chaque creation d'un objet qu'on oblige qu'il ait la fourniture seulement le nom
	de la table à travers le contructeur pas pour la créer directement ou bien inserer directement des donnés
	Cela nous permet de garder le fille sur chacun des objets créer qu'il soit pour les la création proprement 
	dite de la tale on utilise le même nom pour créer la table donc:
	On demande la fonction creation de table fournit un argument qui va désigner le nom table à créer
	On demande egalement un argument à la fonction de l'insertion des données dans la tables pour chaque à travers son nom de table
	Et ainsi de suite pour toutes méthodes de la classe en passant par les query
	Vient le problème des selections: La fonction SELECT ne retourne rien il alors d'abord faire la serlection, stocker le resutat de cette selection dans une variable et par la suite retourner cette variable

	"""

	def __init__(self, table_name):

		try:
			#Connection à la base de données avec les paramètres nécésaaires
			self.connection = psycopg2.connect("dbname = 'formation' user = 'michel' host = 'localhost' password = 'SaintMichel' port ='5432' ")
			
			#C'est ça qui autorise la cr&tion des tbale sinon les fonction vont 100 fois s'exécuter rien ne va se passer
			self.connection.autocommit = True


			# le curseur pour la communication avec la base de données
			self.cursor = self.connection.cursor()

		except:
			pprint("Cant connect dadabase")



		#Le nom de la table à founir lors de l'instanciation d'un object de la classe
		self.table_name = table_name




	def create_table(self, table_name):
		"""
		Methode(fonction de classe) pour la crétion de la table dans la base de données
		le nom table_name est obligation pour pouvoir nommer la table
		si on crée un objet de cette classe, ce objet possede déjà le nom table_name
		on peut l'utiliser pour le nom de la table à savoir self.table_name
		Voici la syntax :
				obj = Create("nom_table")
				obj.create_table(obj.table_name)
		Ce la crée une table dans la basse de données du même nom que l'argument donné à l'instanciation de l'objet
		"""
		self.table_name = table_name
		# print(type(table_name))
		print(type(self.table_name))

		create_commande = " CREATE TABLE " + self.table_name + "( id serial PRIMARY KEY, nom varchar(250), prenom varchar(250), profession varchar(250), age integer NOT NULL, nationalite varchar(250), ville varchar(250), residence varchar(250) )"
		print(type(create_commande))

		try:

			self.cursor.execute(create_commande)

		except psycopg2.ProgrammingError :
			print("Cette table existe déjà")

		# return self.table_name




	def insert_items(self, table_name, nom, prenom, profession, age, nationalite, ville, residence):
		"""

		Méthode pour l'insertion des donnees dans la table de la base de donnees en se basant sur le nom de la
		table self.table_name
		La particularité de cette fonction est qu'elle prend assez de ce qui reste à amélioré
		ces paramètres sont les nom des champs de la base de données
		"""
		self.table_name = table_name
		insert_command = " INSERT INTO " + self.table_name + "(nom, prenom, profession, age, nationalite, ville, residence) VALUES(' " + nom + " ',' " + prenom + " ',' " + profession + " ',' " + age + " ',' " + nationalite + " ',' "+ ville +" ',' "+ residence+" ')"
		print(type(insert_command))
		self.cursor.execute(insert_command)
        # inser_command = " INSERT INTO pet(name, age ) VALUES('" +  new_record[0] + "','" + new_record[1] + "')"




	def query_all(self, table_name):
		"""
		
		Methode pour la selection des objet de la base de donnees dans la table mentionnée self.table_name
		Comme noté haut la commande 	SELECT ne retourne rien ici
		on a profiter l=stocker les données dans la variable donnees pour pouvoir le retourner
		
		"""
		self.table_name = table_name

		self.cursor.execute(" SELECT * FROM " + self.table_name + " ")
		donnees = self.cursor.fetchall()
		for donnee in donnees:
			pprint("Les données sont : {}".format(donnee))
		return donnees

			












if __name__ == '__main__':


	new_table = Create("liste")

	# new_table.create_table(new_table.table_name)
	new_table.insert_items(new_table.table_name, nom="Michel", prenom="Excellence", profession="Geek", age="23", nationalite="Guinéene", ville="Marrakech", residence="Saada")

	pprint(new_table.query_all(new_table.table_name))

