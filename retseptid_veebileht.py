from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

#----------------------Andmebaasid------------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///retseptid.db'
db = SQLAlchemy(app)

class Retseptid(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(100), unique=True, nullable=False)
    vegan = db.Column(db.Boolean, nullable=False, default=False)
    keto = db.Column(db.Boolean, nullable=False, default=False)
    gluteenivaba = db.Column(db.Boolean, nullable=False, default=False)
    paleo = db.Column(db.Boolean, nullable=False, default=False)
    lchf = db.Column(db.Boolean, nullable=False, default=False)
    laktoosivaba = db.Column(db.Boolean, nullable=False, default=False)
#----------------------Veebisaidid------------------

#Avaleht
@app.route('/')
def index() :
    return render_template('avaleht.html')

#Otsi retsepte leht
@app.route('/retseptid')
def retseptid() :
    return render_template('retseptid.html')

#Retseptide otsingu tulemus
@app.route('/retseptid_tulemused', methods=['GET', 'POST'])
def retseptid_tulemused() :
    retseptid_search = []
    return render_template('retseptid_tulemused.html', retseptid=retseptid_search)

if __name__ == '__main__':
    app.run()