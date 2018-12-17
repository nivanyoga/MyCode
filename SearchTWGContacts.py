import os
import fileinput
import mysql.connector


path = "C:\\HP_WORKLAPTOP\\PERSONAL\\TWG_EVENT_2018\\"
exts = [".csv"]
os.chdir('C:\\HP_WORKLAPTOP\\PERSONAL\\TWG_EVENT_2018\\')


filenames = []

#print(filenames)

conn=mysql.connector.connect(user='root', password='XXXX',host='localhost',database='nivan')
mycursor = conn.cursor()

sql = ""
desc = ""
size = 0
amount = 0.0
balance = 0.0

for root, dirs, files in os.walk(os.path.expanduser(path)):
    for fn in files:
        #print (root);
        if root.find("Contacts") > 0:
            #print (root+"\\"+fn)
            wipfilename = root+"\\"+fn
            bn, ext = os.path.splitext(fn)
            #print (ext)
            if (ext == exts[0]) and fn.startswith("twg_act_contacts2018"):
                filenames.append(fn)

                for line in fileinput.input(wipfilename):
                    if line.startswith("Date"):
                        continue
                    line.replace('"', '')
                    trans = line.split(",")
                    #print (trans.__len__())

                    print (trans[trans.__len__()-1].replace('"', ''))
                    size = len(trans)

                    # dateparts = trans[0].split("/")
                    # date_str = "%s%s%s" %(dateparts[2],dateparts[1],dateparts[0])
                    # desc = trans[1].replace("\"", "")
                    # desc = desc.replace("\'", "")
                    # #print ("desc=", desc)
                    #
                    # if size <= 4:
                    #     amount = trans[2]
                    #     balance = trans[3].replace("\n", "")
                    # else:
                    #     desc += " "
                    #     desc += trans[2].replace("\'", "")
                    #     amount = trans[3]
                    #     balance = trans[4].replace("\n", "")
                    #
                    # balance = trans[3].replace("\n", "")
                    # sql = "INSERT INTO nivan.firstdirecttransaction (trans_date, description, amount, balance) VALUES('" + \
                    #       date_str + "','" + desc + "'," + amount + "," + balance + ");"
                    #
                    # print ("AFTER=", sql)
                    # try:
                    #     mycursor.execute(sql)
                    #     conn.commit()
                    # except (RuntimeError, TypeError, NameError, ValueError):
                    #     continue
                    # else:
                    #     continue



mycursor.close()
conn.close()

