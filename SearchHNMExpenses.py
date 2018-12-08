
__author__ = 'Nivan'


import os
import io
import fileinput
import math
import csv
import glob
import dateutil
import calendar
import smtplib
import datetime
import mysql.connector

import matplotlib.pyplot as plt
import numpy as np

from dateutil import parser
dt = parser.parse("Aug 28 1999 12:00AM")

path = "C:\\HMN CONSULTING\\InvoicesExpenses\\2015"
exts = [".csv"]

#filenames = os.listdir('.')

filenames = []

#print(filenames)

#conn=mysql.connector.connect(user='root', password='Nirupan1',host='localhost',database='nivan')
conn=mysql.connector.connect(user='root', password='Hannah10072002',host='localhost',database='nivan')
mycursor = conn.cursor()

sql = ""
size = 0
old_balance ="-1"

for root, dirs, files in os.walk(os.path.expanduser(path)):
    for fn in files:
        #print (root);
        if root.find("InvoicesExpenses") > 0:
            #print (root+"\\"+fn)
            wipfilename = root+"\\"+fn
            bn, ext = os.path.splitext(fn)
            #print (ext)
            if (ext == exts[0]) and fn.startswith("Expenses"):
                #print (fn)
                filenames.append(fn)
                with open(wipfilename, newline='') as f:
                    reader = csv.reader(f)
                    for trans in reader:
                        date_str, desc, claimed = trans
                        print (date_str, desc, claimed)
                        if (date_str == "Date"):
                            continue

                        claimed= claimed.replace(" ", '0.0')
                        #print (balance)

                        sql = "INSERT INTO nivan.hmnexpenses " \
                              "(trans_date, description, amount_claimed)" \
                              " VALUES( " + \
                              "STR_TO_DATE('" + date_str + "', '%d/%m/%Y')" +  ",'" + \
                              desc + "'," + claimed + ");"

                        print ("AFTER=", sql)

                        try:
                            mycursor.execute(sql)
                            conn.commit()
                        except (RuntimeError, TypeError, NameError, ValueError):
                            continue
                        else:
                            continue

mycursor.close()
conn.close()

