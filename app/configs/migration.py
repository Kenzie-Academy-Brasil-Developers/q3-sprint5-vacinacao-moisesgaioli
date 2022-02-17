from flask import Flask
from flask_migrate import Migrate

def init_ap(app: Flask):
    
    Migrate(app=app, db=app.db)

    