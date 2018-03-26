#! /usr/bin/python

#-*-coding:utf-8-*-


from PyQt5.QtCore import QDateTime, QDate, QTime, Qt 



datetime = QDateTime.currentDateTime()

print(datetime) #Le format date de PyQt5

print(datetime.toString())#Modelisation sans paramètre

print(datetime.toString(Qt.ISODate)) #Le format date ISO

print(datetime.toString(Qt.DefaultLocaleLongDate)) #Le format local en tenant compte de la culture local



date = QDate.currentDate() #La date seulement

print(date)

print(date.toString(Qt.DefaultLocaleLongDate))


time = QTime.currentTime()

print(time)
print(time.toString())
print(time.toString(Qt.DefaultLocaleLongDate))