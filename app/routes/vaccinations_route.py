from flask import Blueprint
from app.controllers import vaccinations_controller


bp = Blueprint('vaccinations', __name__, url_prefix='/vaccinations')


bp.get('')(vaccinations_controller.get_vaccinations)
bp.post('')(vaccinations_controller.post_vaccinations)