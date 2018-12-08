__author__ = 'DEFAULT'
import math
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector


conn=mysql.connector.connect(user='root', password='Mira07051964',host='localhost',database='nivan')
mycursor = conn.cursor()
sql = "select * from nivan.firstdirecttransaction where trans_date BETWEEN '20070101' and '20180101' " \
      "and description LIKE '%NATIONWIDE%' order by trans_date desc"

mycursor.execute(sql)
trans = []

amt = 0.0

fig, ax = plt.subplots()
#plt.yscale('linear')

row = mycursor.fetchone()
i=0
while row is not None:
    #print(row)
    #print ( row[0], row[3])
    #trans.append(row)
    amt = math.fabs(row[0])
    ax.plot(amt, row[2], '-o', ms=5, lw=5, alpha=0.7, mfc='orange')
    row = mycursor.fetchone()

mycursor.close()
conn.close()

ax.set(xlabel='date', ylabel='balance',
       title='First Direct Trans')
ax.grid()
plt.show()