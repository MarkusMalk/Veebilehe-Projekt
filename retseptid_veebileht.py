from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from sqlalchemy.engine import Engine


app = Flask(__name__)
#----------------------Andmebaasid-----------------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///retseptid.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@event.listens_for(Engine, "connect")
def enable_foreign_keys(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

class Retseptid(db.Model) :
    __tablename__ = 'retseptid'

    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(150), unique=True, nullable=False)
    pilt = db.Column(db.String(255), nullable=False)
    juhised = db.Column(db.Text, nullable=False)

    dieedid = db.relationship('Dieedid', secondary='retsepti_dieedid', back_populates='retseptid')
    koostisosad = db.relationship('Retsepti_koostisosad', back_populates='retsept', cascade='all, delete-orphan')


class Dieedid(db.Model) :
    __tablename__ = 'dieedid'

    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(20), unique=True, nullable=False) #vegan, keto, gluteenivaba, paleo, lchf, laktoosivaba

    retseptid = db.relationship('Retseptid', secondary='retsepti_dieedid', back_populates='dieedid')


class Retsepti_dieedid(db.Model) :
    __tablename__ = 'retsepti_dieedid'
    retsepti_id = db.Column(db.Integer, db.ForeignKey('retseptid.id', ondelete='CASCADE'), primary_key=True)
    dieedi_id = db.Column(db.Integer, db.ForeignKey('dieedid.id', ondelete='CASCADE'), primary_key=True)

class Koostisosad(db.Model):
    __tablename__ = 'koostisosad'

    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(100), nullable=False, unique=True)

class Retsepti_koostisosad(db.Model):
    __tablename__ = 'retespti_koostisosad'

    retsepti_id = db.Column(db.Integer, db.ForeignKey('retseptid.id'), primary_key=True)
    koostisosa_id = db.Column(db.Integer, db.ForeignKey('koostisosad.id'), primary_key=True)
    kogus = db.Column(db.Float, nullable=False)
    uhik = db.Column(db.String(30), nullable=False)

    retsept = db.relationship('Retseptid',back_populates='koostisosad')
    koostisosa = db.relationship('Koostisosad')


with app.app_context():
    Dieedid.query.filter_by(nimi="vagan").update(
        {"nimi": "vegan"}
    )

    db.session.commit()
    db.create_all()

#----------------------Veebisaidid------------------

#Avaleht
@app.route('/')
def index() :
    return render_template('avaleht.html')

#Otsi retsepte leht
@app.route('/retseptid')
def retseptid() :
    retseptid = Retseptid.query.all()
    return render_template('retseptid.html', retseptid=retseptid)

#Retseptide otsingu tulemus
@app.route('/retseptid_tulemused', methods=['GET', 'POST'])
def retseptid_tulemused() :
    retseptid_search = []
    return render_template('retseptid_tulemused.html', retseptid=retseptid_search)


if __name__ == '__main__':
    app.run()