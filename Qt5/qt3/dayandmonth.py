#! /usr/python

#-*-conding:utf-8-*-

from PyQt5.QtCore import QDate


date = QDate.currentDate()


d= QDate(2018, 3, 22)

print("Days in month : {}".format(d.daysInMonth()))


print("Days in a year : {} ".format(d.daysInYear()))
