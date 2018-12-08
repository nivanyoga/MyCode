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

path = "C:\\HMN CONSULTING\BankStatements\\Statements"
exts = [".csv"]

#filenames = os.listdir('.')

filenames = []

#print(filenames)

#conn=mysql.connector.connect(user='root', password='Nirupan1',host='localhost',database='nivan')
#conn=mysql.connector.connect(user='root', password='Nivan22121965',host='localhost',database='nivan')
conn=mysql.connector.connect(user='root', password='Hannah10072002',host='localhost',database='nivan')

mycursor = conn.cursor()

sql = ""
size = 0
old_balance ="-1"

for root, dirs, files in os.walk(os.path.expanduser(path)):
    for fn in files:
        #print (root);
        if root.find("BankStatements") > 0:
            #print (root+"\\"+fn)
            wipfilename = root+"\\"+fn
            bn, ext = os.path.splitext(fn)
            #print (ext)
            if (ext == exts[0]) and fn.startswith("Transactions52_52"):
                #print (fn)
                filenames.append(fn)
                with open(wipfilename, newline='') as f:
                    reader = csv.reader(f)
                    for trans in reader:
                        date_str, type, desc, paid_out, paid_in, balance = trans
                        #print (date_str, type, desc, paid_in, paid_out, balance)
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

                        sql = "INSERT INTO nivan.hsbctransaction " \
                              "(trans_date, trans_type, description, paid_out_amount, paid_in_amount, balance)" \
                              " VALUES(" + \
                              "STR_TO_DATE('" + date_str + "', '%d %M %Y')" + ",'"  + type + "','" + \
                              desc + "'," + paid_out + "," + paid_in + "," + balance + ");"

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

"""
                        size = len(trans)
                        date_str = trans[0].replace('"', '')

                        type = trans[1]
                        desc = trans[2].replace("\"", "")
                        desc = desc.replace("\'", "")
                        paid_out =  trans[3].replace('"', '').replace(" ", '0.0')
                        #paid_out = trans_paid_out.format("%lf")
                        paid_in = (trans[4].replace('"', '')).replace(" ", '0.0')
                        balance = (trans[5].replace('"', '').replace("\n", "")).replace(" ", '0.0')
"""

