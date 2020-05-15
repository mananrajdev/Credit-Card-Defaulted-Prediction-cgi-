#!C:\Users\manan\AppData\Local\Programs\Python\Python36\python.exe
print("Content-type:text/html \n")
import cgi
form=cgi.FieldStorage()
deff=form.getvalue("deff")


if int(deff)==0:
    print("""
    <html>
    <head>
    	<link rel="stylesheet" type="text/css" href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">
    
    	<link rel="shortcut icon" href="card_icon.ico" />
    	<title>	Creditcard Defaulter?</title>
    
    </head>
    <body style="background-color: #95f895">
    	
    
    	<div class="col-md-4">
    		<img src="creditcard_image1.png" class="image">
    	</div>
    	<div class="col-md-4" style="margin-top: 100px; font-size: 40px; color: blue">
    		<label>YOU ARE NOT A DEFAULTER!</label>
    	</div>
    	<div class="col-md-4">
    		<img src="creditcard_image2.png" class="image">
    	</div>
    </body>
    </html>      
    
    """)
    
if int(deff)==1:
    print("""
    <html>
    <head>
    	<link rel="stylesheet" type="text/css" href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">
    
    	<link rel="shortcut icon" href="card_icon.ico" />
    	<title>	Creditcard Defaulter?</title>
    
    </head>
    <body style="background-color: #95f895">
    	
    
    	<div class="col-md-4">
    		<img src="creditcard_image1.png" class="image">
    	</div>
    	<div class="col-md-4" style="margin-top: 100px; font-size: 40px; color: red">
    		<label>YOU ARE A DEFAULTER!</label>
    	</div>
    	<div class="col-md-4">
    		<img src="creditcard_image2.png" class="image">
    	</div>
    </body>
    </html>      
    
    """)
