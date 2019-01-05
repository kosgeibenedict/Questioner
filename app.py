from flask import Flask, render_template, request, session, logging, url_for,redirect
from passlib.hash import sha256_crypt

app = Flask(__name__)

@app.route('/')
def signup():
    return render_template('register.html')

if __name__=="__main__":
    app.run(debug=True)
