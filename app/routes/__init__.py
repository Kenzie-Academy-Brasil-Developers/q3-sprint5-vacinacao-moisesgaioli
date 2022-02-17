from flask import Flask, Blueprint
from app.routes.vaccinations_route import bp as bp_vaccinations


bp_api = Blueprint('api', __name__, url_prefix='/api')

def init_app(app: Flask):

    bp_api.register_blueprint(bp_vaccinations)
    
    app.register_blueprint(bp_api)