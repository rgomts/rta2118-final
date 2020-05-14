# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@autor : etill
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/1006")
def home():
     return render_template("home.html")

 
@app.route("/movies")
def classes():
     return render_template("movies.html")

@app.route("/tv")
def assignments():
     return render_template("tv.html")



#start the server
if __name__ == "__main__":
    app.run(debug = True)