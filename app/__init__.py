from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData, Table

app = Flask(__name__,instance_relative_config = True )
print(app.config.from_pyfile('config.py'))
engine = create_engine('mysql://anonymous@ensembldb.ensembl.org:3306/ensembl_website_97')
metadata = MetaData(bind=engine)
print(engine, metadata)
from app import views
