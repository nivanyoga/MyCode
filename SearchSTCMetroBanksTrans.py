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

path = "C:\\HP_WORKLAPTOP\\PERSONAL\\StColumba\\Accounts\\Bank Statements\\2018\\CSV"
exts = [".csv"]


filenames = []

#conn=mysql.connector.connect(user='root', password='Mira07051964',host='localhost',database='nivan')
conn=mysql.connector.connect(user='root', password='Hannah10072002',host='localhost',database='nivan')

mycursor = conn.cursor()

sql = ""
size = 0
old_balance ="-1"

for root, dirs, files in os.walk(os.path.expanduser(path)):
    for fn in files:
        #print (root);
        if root.find("Bank Statements") > 0:
            #print (root+"\\"+fn)
            wipfilename = root+"\\"+fn
            bn, ext = os.path.splitext(fn)
            #print (ext)
            if (ext == exts[0]) and fn.startswith("Transaction_"):
                #print (fn)
                filenames.append(fn)
                header = 1
                with open(wipfilename, newline='') as f:
                    reader = csv.reader(f)
                    for trans in reader:

                        if (header == 1):
                            header = 0
                            continue

                        date_str, ref, type, paid_in, paid_out, balance = trans
                        print (date_str, type, ref, paid_in, paid_out, balance)
                        if (date_str == "Date"):
                            continue

                        paid_out=paid_out.replace(" ", '0.0')
                        paid_in=paid_in.replace(" ", '0.0')
                        balance=balance.replace(" ", '0.0')
                        #print (balance)

                        if balance == '0.0':
                            balance_amt = float(old_balance)-float(paid_out)+float(paid_in)
                            balance = str( balance_amt )

                        old_balance=balance

                        sql = "INSERT INTO nivan.stcmetrotransaction " \
                              "(trans_date, reference, trans_type, money_in_amt, money_out_amt, balance)" \
                              " VALUES(" + \
                              "STR_TO_DATE('" + date_str + "', '%d/%m/%Y')" + ",'"  + ref + "','" + \
                              type + "'," + paid_in + "," + paid_out + "," + balance + ");"

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


