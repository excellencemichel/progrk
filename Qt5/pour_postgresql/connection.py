import psycopg2 #Module de gestion de base de données pour posgrest

from pprint import  pprint

class DatabaseConnexion:
    """
    Une classe pour se connecter à la base de données
    """

    def __init__(self):

        try:
            self.connection = psycopg2.connect(
                                               "dbname = 'formation' user = 'michel' host = 'localhost' password = 'SaintMichel' port ='5432' "
                                               )

            self.connection.autocommit = True
            self.cursor = self.connection.cursor()


        except:
            pprint("Cannot connect to database")


    def create_table(self):
        """
        Création d'une table dans la base de donnée
        le module psycopg2 donne une erruer il faut
        complèter avec psycopg2-banary
        :return:
        """
        create_table_command = "CREATE TABLE pet( id serial PRIMARY KEY, name varchar(100), age integer NOT NULL )"
        print("Son type est : ", type(create_table_command))
        self.cursor.execute(create_table_command)


    def inser_new_record(self):
        """
        Insertion de nouvelle rentrée dans la base de donnée
        :return:
        """

        new_record = ["Pierre", "12"]


        inser_command = " INSERT INTO pet(name, age ) VALUES('" +  new_record[0] + "','" + new_record[1] + "')"
        pprint(inser_command)
        self.cursor.execute(inser_command)


    def query_all(self):
        """
        Requete de selection des données dans la table
        :return:
        """
        self.cursor.execute("SELECT * FROM pet")
        pets = self.cursor.fetchall()

        for pet in pets:
            pprint("Each pet: {}".format(pet))


    def updade_record(self):
        """
        Requete de mise en jour des données dans la table
        :return:
        """
        update_command = "UPDATE pet SET age=400 WHERE id=1"
        self.cursor.execute(update_command)


    def drop_table(self):
        """
        Suppression de la table dans le base de base de données
        :return:
        """

        drop_table_command = "DROP TABLE pet"

        self.cursor.execute(drop_table_command)



if __name__=="__main__":
    database_connection = DatabaseConnexion()
    # database_connection.create_table() #Pour ne pas chaque fois relencer la fonction
    database_connection.inser_new_record() #Pour ne pas chaque fois relancer la foction
    # database_connection.updade_record()
    database_connection.query_all()
    database_connection.drop_table() #On commente pour ne pas supprimer la table dans la base de données
