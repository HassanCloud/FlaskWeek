from flask import Flask # Import Flask class
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy class

app = Flask(__name__) # create Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
 
db = SQLAlchemy(app) # Create SQLALchemy object

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)

class People(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(747), nullable=False)
        alive = db.Column(db.Boolean, default=True)
        height = db.Column(db.Float)

if __name__=='__main__':
    app.run(debug==True)