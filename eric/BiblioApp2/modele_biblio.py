# -*- coding:utf-8 -*-

#Standard import
from os import path as os_path
from collections import namedtuple, OrderedDict
import json


#Library import
from PyQt5.QtCore import Qt,  QAbstractTableModel, QModelIndex,  QVariant
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


NOM_FICHIER_DB = "bibliotheque.db"

Livre = namedtuple("Livre", ("idLivre", "titre",  "auteur",  "editeur",  "genre", 
                            "annee", "resume",  "prix")
                    )


class ModeleTableBiblio(QAbstractTableModel):
    def __init__(self):
        super(ModeleTableBiblio,  self).__init__()
        self.titresColonnes = ("Titre",  "Auteur", "Editeur")
        self.livres = None
        self.idParGenre = None

        bdExiste = os_path.exists(NOM_FICHIER_DB)
        bd = QSqlDatabase.addDatabase("QSQLITE")
        bd.setDatabaseName(NOM_FICHIER_DB)
        bd.open()
        if not bdExiste:
            self.creeBD()
        self.litBD()

    
    def headerData(self,  section,  orientation,  role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.titresColonnes[section]
        return QVariant()
    
    def columnCount(self, parent):
        return len(self.titresColonnes)
        
    def rowCount(self,  parent):
        return len(self.livres)
    
    def data(self,  index,  role):
        if role == Qt.DisplayRole and index.isValid():
            return self.livres[index.row()][index.column()+1]
        return QVariant()


    
    def ajouterLivre(self, livre):
        query = QSqlQuery()
        query.prepare(""" INSERT INTO  books
            (book_id, title, author, publisher,
            genre_id, year, summary, price)
            VALUES (NULL, :titre, :auteur, :editeur,
            :idGenre, :annee, :resume, :prix)

            """)
        query.bindValue(":titre", livre.titre)
        query.bindValue(":auteur", livre.auteur)
        query.bindValue(":editeur", livre.editeur)
        query.bindValue(":idGenre", self.idParGenre[livre.genre])
        query.bindValue(":annee", livre.annee)
        query.bindValue(":resume", livre.resume)
        query.bindValue(":prix", livre.prix)

        query.exec_()

        idLivre = query.lastInsertId()
        livre = Livre(idLivre, *livre[1:])
        indiceLivre = len(self.livres)
        self.beginInsertRows(QModelIndex(), indiceLivre, indiceLivre)
        self.livres.append(livre)
        self.endInsertRows()



    def supprimerLivre(self, indiceLivre):
        query = QSqlQuery()
        query.prepare(""" DELETE FROM books 
                    WHERE book_id = :idLivre """)

        query.bindValue(":idLivre", self.livres[indiceLivre].idLivre)
        query.exec_()

        self.beginRemoveRows(QModelIndex(), indiceLivre, indiceLivre)
        del self.livres[indiceLivre]
        self.endRemoveRows()


    def remplaceLivre(self, indiceLivre, livre):
        query = QSqlQuery()
        query.prepare(""" UPDATE books 
                    SET title =:titre,
                    author=:auteur,
                    publisher =:editeur,
                    genre_id =:idGenre,
                    year =:annee,
                    summary =:resume,
                    price =:prix
                    WHERE book_id =:idLivre """ )
        query.bindValue(":idLivre", self.livres[indiceLivre].idLivre)
        query.bindValue(":titre", livre.titre)
        query.bindValue(":auteur", livre.auteur)
        query.bindValue(":editeur", livre.editeur)
        query.bindValue(":idGenre", self.idParGenre[livre.genre])
        query.bindValue(":annee", livre.annee)
        query.bindValue(":resume", livre.resume)
        query.bindValue(":prix", livre.prix)

        query.exec_()
        self.livres[indiceLivre] = livre
        self.dataChanged.emit(self.createIndex(indiceLivre,0), self.createIndex(indiceLivre, 2))



    def creeBD(self):
        QSqlQuery(""" CREATE TABLE genres 
                (genre_id INTEGER PRIMARY KEY,
                genre TEXT)""")

        QSqlQuery(""" CREATE TABLE books 
                 (book_id INTEGER PRIMARY KEY,
                  title TEXT, author TEXT,
                  publisher TEXT, genre_id INTEGER,
                  year INTEGER, summary TEXT,
                 price FLOAT ) """)

        QSqlQuery(""" INSERT INTO genres
                 (genre) VALUES ("---"), 
                 ("Biographie"), ("Fantastique"),
                ("Historique"), ("Policier"),
                 ("Science-Fiction")""")



    def litBD(self):
        query = QSqlQuery(""" SELECT genre_id,
             genre FROM genres ORDER BY genre_id""")

        self.idParGenre = OrderedDict()
        while query.next():
            self.idParGenre[query.value(1)] = query.value(0)

        query = QSqlQuery(""" SELECT book_id, title,
                     author, publisher, genre, year,
                     summary, price FROM books JOIN 
                     genres ON genres.genre_id = books.genre_id
                     """)


        self.livres = []
        while query.next():
            livre = Livre(*(query.value(i) for i in range(8)))
            self.livres.append(livre)



    def genres(self):
        return self.idParGenre.keys()
