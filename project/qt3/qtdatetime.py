#! /usr/bin/python

#-*-coding:utf-8-*-



from PyQt5 import QtWidgets, QtGui, QtCore




datetime = QtCore.QDateTime.currentDateTime()

print (datetime.toString())



date = QtCore.QDate.currentDate()
print (date.toString())



print("Loacal Date and Time is : ", datetime.toString(QtCore.Qt.DefaultLocaleLongDate))


print("Universal Date and Time is : ", datetime.toUTC().toString())

print("The offset From UTC is {} : Seconds".format(datetime.offsetFromUtc()))