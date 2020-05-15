#!C:\Users\manan\AppData\Local\Programs\Python\Python36\python.exe
print("Content-type:text/html \n")
import cgi
import mysql.connector

f=cgi.FieldStorage()
idd= f.getvalue("idd")
passs= f.getvalue("pass")


myDB=mysql.connector.connect(host="localhost", user="root", passwd="", charset="utf8", database="carproj")
mysql=myDB.cursor()

mysql.execute('select email from user_data')
all_id=mysql.fetchall()

if idd in all_id[0]:
    mysql.execute('select password from user_data where email="%s"'%idd)
    pass1=mysql.fetchone()
    if passs==pass1[0]:
        redirectURL= "http://localhost/creditcard_project/creditcard_main.html"

else:
    redirectURL= "http://localhost/creditcard_project/creditcard_login.html"
    

print("<html>")
print("<head>")
print('<meta http-equiv="refresh" content="0;url='+str(redirectURL)+'"/>')
print("</head>")
print("</html>")
