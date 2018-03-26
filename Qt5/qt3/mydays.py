#! /usr/python

#-*-conding:utf-8-*-


from PyQt5.QtCore import QDateTime, Qt


datetime = QDateTime.currentDateTime()


print("Today is {}".format(datetime.toString(Qt.ISODate)))

print("Add 12 days to the date : {}".format(datetime.addDays(12).toString(Qt.ISODate)))

print("Subtracting 25 days {} ".format(datetime.addDays(-25).toString(Qt.ISODate)))

print("Add 50 second {} ".format(datetime.addSecs(50).toString(Qt.ISODate)))

print("Addind 3 month {} ".format(datetime.addMonths(3).toString(Qt.ISODate)))
print("Addin 3 years {} ".format(datetime.addYears(3).toString(Qt.ISODate)))
