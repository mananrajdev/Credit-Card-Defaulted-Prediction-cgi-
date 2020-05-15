#!C:\Users\manan\AppData\Local\Programs\Python\Python36\python.exe
print("Content-type:text/html \n")
import cgi
import pickle

f=cgi.FieldStorage()
limit_bal=f.getvalue("limit_bal")
sex=f.getvalue("sex")
education=f.getvalue("education")
marriage=f.getvalue("marriage")
age=f.getvalue("age")
pay_0=f.getvalue("pay_0")
pay_1=f.getvalue("pay_1")
pay_2=f.getvalue("pay_2")
pay_3=f.getvalue("pay_3")
pay_4=f.getvalue("pay_4")
pay_5=f.getvalue("pay_5")
billamt_1=f.getvalue("billamt_1")
billamt_2=f.getvalue("billamt_2")
billamt_3=f.getvalue("billamt_3")
billamt_4=f.getvalue("billamt_4")
billamt_5=f.getvalue("billamt_5")
billamt_6=f.getvalue("billamt_6")
payamt_1=f.getvalue("payamt_1")
payamt_2=f.getvalue("payamt_2")
payamt_3=f.getvalue("payamt_3")
payamt_4=f.getvalue("payamt_4")
payamt_5=f.getvalue("payamt_5")
payamt_6=f.getvalue("payamt_6")

with open('check.pk1', 'rb') as f:
   x=pickle.load(f)

y_pred=x.predict([[int(limit_bal), int(sex), int(education), int(marriage), int(age), int(pay_0), int(pay_1), int(pay_2), int(pay_3), int(pay_4), int(pay_5), int(billamt_1), int(billamt_2), int(billamt_3), int(billamt_4), int(billamt_5), int(billamt_6), int(payamt_1), int(payamt_2), int(payamt_3), int(payamt_4), int(payamt_5), int(payamt_6),]])



redirectURL= "http://localhost/creditcard_project/creditcard_final.py?deff={}".format(abs(y_pred[0]))
print("<html>")
print("<head>")
print('<meta http-equiv="refresh" content="0;url='+str(redirectURL)+'"/>')
print("</head>")
print("</html>")


