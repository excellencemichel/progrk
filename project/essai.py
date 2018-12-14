import psycopg2


class Personne:

    def __init__(self, dbname, user, host, password, port):
        self.dbname = dbname
        self.user = user
        self.host = host
        self.password = password
        self.port = port




    def connexion(self):

        try:
            conn = psycopg2.connect("dbname = '{dbname}' user = '{user}' host = '{host}' password = '{password}' port ='{port}' ".format(dbname=self.dbname, user=self.user, host=self.host, password=self.password, port=self.port))
            conn.autocommit = True
            cursor = conn.cursor()

            self.cursor= cursor

        except:
            raise print("Can't connect database !")







