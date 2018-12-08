import os
import io
import fileinput
import math
import csv
import glob
import dateutil
import calendar
import smtplib
import mysql.connector

##from lxml import html
import requests

import matplotlib.pyplot as plt
import numpy as np


path = "C:\\HP_WORKLAPTOP\\PERSONAL\\FirstDirect\\"
exts = [".CSV"]
os.chdir('C:\HP_WORKLAPTOP\PERSONAL\FirstDirect\April 2018 to April 2019')
#filenames = os.listdir('.')

filenames = []

#print(filenames)

#conn=mysql.connector.connect(user='root', password='Nivan22121965',host='localhost',database='nivan')
#conn=mysql.connector.connect(user='root', password='Mira07051964',host='localhost',database='nivan')
conn=mysql.connector.connect(user='root', password='Hannah10072002',host='localhost',database='nivan')
mycursor = conn.cursor()

sql = ""
desc = ""
size = 0
amount = 0.0
balance = 0.0

"""
SELECT count(*) FROM firstdirecttransaction
TRUNCATE TABLE firstdirecttransaction
INSERT INTO nivan.firstdirecttransaction (trans_date, description, amount, balance) VALUES('20120606','TESCO STORES 5780         ACTON',-3.40,2356.16);
CREATE UNIQUE INDEX trans_idx ON nivan.firstdirecttransaction (trans_date,description,amount,balance)
DROP INDEX trans_idx
"""


for root, dirs, files in os.walk(os.path.expanduser(path)):
    for fn in files:
        #print (root);
        if root.find("April") > 0:
            #print (root+"\\"+fn)
            wipfilename = root+"\\"+fn
            bn, ext = os.path.splitext(fn)
            #print (ext)
            if (ext == exts[0]) and fn.startswith("Historical201811"):
            #if (ext == exts[0]) and fn.startswith("20171229"):
                #print (fn)
                filenames.append(fn)

                for line in fileinput.input(wipfilename):
                    if line.startswith("Date"):
                        continue
                    line.replace('"', '')
                    trans = line.split(",")
                    #print (trans)
                    size = len(trans)
                    #a.append(trans[0])
                    #b.append(trans[3].replace("\n", ""))

                    dateparts = trans[0].split("/")
                    date_str = "%s%s%s" %(dateparts[2],dateparts[1],dateparts[0])
                    desc = trans[1].replace("\"", "")
                    desc = desc.replace("\'", "")
                    #print ("desc=", desc)

                    if size <= 4:
                        amount = trans[2]
                        balance = trans[3].replace("\n", "")
                    else:
                        desc += " "
                        desc += trans[2].replace("\'", "")
                        amount = trans[3]
                        balance = trans[4].replace("\n", "")
                        
                    balance = trans[3].replace("\n", "")
                    #trans[1] = trans[1].replace(",", "")
                    #trans[1] = trans[1].replace("@", "")

                    #print ("COUNT=", size)
                    sql = "INSERT INTO nivan.firstdirecttransaction (trans_date, description, amount, balance) VALUES('" + \
                          date_str + "','" + desc + "'," + amount + "," + balance + ");"

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

# for f in glob.glob("*.csv"):
#	concat = ''.join([open(f).read() for f in files])
#         os.system("cat "+f+" >> AllTrans.csv")


outfilename = "FoundTrans.csv"
print(outfilename)

with open(outfilename, 'w') as fout:
    for line in fileinput.input(filenames):
#        print (line)
        #trans = line.split(",")
        #print (trans[0] + "=" + trans[3] )

        if line.find("Date") != 0:
            fout.write(line)

print ("***********************OUTPUT*****************************************")


a = []
b = []

with open(outfilename, 'r') as fin:
    #for line in fileinput.input(outfilename):
    for line in fileinput.input(filenames):
        line.replace('"', '')
        trans = line.split(",")
        a.append(trans[0])
        b.append(trans[3].replace("\n", ""))

        dateparts = trans[0].split("/")
        #print (dateparts)
        date_str = "%s%s%s" %(dateparts[2],dateparts[1],dateparts[0])
        #print (date_str)

        trans[1] = trans[1].replace("\"", "")
        trans[1] = trans[1].replace(",", "")
        #trans[1] = trans[1].replace("@", "")
        print (trans[1])

        sql = "INSERT INTO nivan.firstdirecttransaction (trans_date, description, amount, balance) VALUES('" + \
              date_str + "','" + trans[1] + "'," + trans[2] + "," + trans[3] + ");"
        print (sql)
        mycursor.execute(sql)
        conn.commit()



mycursor.close()
conn.close()

#print (a)
#print (b)

#plt.plot(a, b)
#plt.show()

#print (calendar.month(1965,12))

#print (calendar.month(2002,7))

#print (calendar.month(1967,1))

#print (calendar.month(1964,5))

#print (calendar.month(1969,2))


#print (calendar.month(1968,2))

#print (calendar.calendar(2015,2,1,10))


#server=smtplib.SMTP("smtp.gmail.com",587)
#server.starttls()

#server.login("nivan1234@gmail.com", "Mirjana1234")

#server.login("miranivan@gmail.com", "Mirjana1")

#server.sendmail("nivan1234@gmail.com", "miranivan@gmail.com", "Please check your Google Drive with Photos", "YESTERDAYS PHOTOS")


#conn=mysql.connector.connect(user='root', password='Nirupan1',host='localhost',database='Nivan')

#print (conn.get_server_version())
#print (conn.get_server_info())

#mycursor = conn.cursor()
#mycursor.execute("show tables")
#mycursor.execute("show variables")
#print(mycursor.fetchall())

"""