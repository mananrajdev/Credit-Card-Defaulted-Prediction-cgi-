# Credit-Card-Defaulted-Prediction-cgi-
Credit Card Defaulter predictions with login page.
The Program uses CGI, HTML and CSS to build an interactive web page. It uses python machine learning algorithms to predict the credit card defaulters.

----------------Requirements----------------
XAMPP- https://www.apachefriends.org/index.html
Python - Version 3.6.5
	Libraries: mysql, cgi, sklearn, pickle
MySQL - Version 8


----------------Code Organisation----------------
HTML Files-
1) creditcard_login.html - It opens the login page (quite similar to facebook login page)

2) creditcard_main.html - It is the main inteface for the credit card information.


Python Files-
1) creditcard_login.py - This file contains the code for checking the ids and passwords sent from creditcard_login.html page.

2) creditcard_ml.py - It creates a machine learning model from the data in "credit-card-default prediction.csv" and saves it using pickle library.

3) creditcard_objectfile.py - It gets all the variables used for machine learning from the creditcard_main.html page and predits the result using machine learning model built in creditcard_ml.py and sends the result to creditcard_final.py.

4) creditcard_final.py - It gets the result from creditcard_objectfile.py and prints it on the webpage using HTML.


----------------Steps to Run the program----------------
Step 1) 
Download xampp and place the following folder in the "ht_docs".

Step 2)
Create a mysql database named "user_data" with 2 columns: "email" & "password". Insert your email ids and corresponding passwords.

Step 3)
In any web browser open the following link - "localhost/creditcard_login".



