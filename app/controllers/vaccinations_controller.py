from flask import request, jsonify
from sqlalchemy.exc import DataError, IntegrityError
from http import HTTPStatus
from app.models.vaccinations_model import VaccineCards
from app.configs.database import db
from app.models.exc import CpfFormatError, KeyFoundError, KeysFormatError, RequestError

def get_vaccinations():
    
    vaccine_cards = VaccineCards.query.all()

    return jsonify(vaccine_cards), HTTPStatus.OK




def post_vaccinations():
    data = request.get_json()

    try:
        vaccine_card = VaccineCards(**data)

        db.session.add(vaccine_card)
        db.session.commit()

        return jsonify(vaccine_card), HTTPStatus.CREATED

    except IntegrityError:
        return {'error': "cpf already exists"}, HTTPStatus.CONFLICT
    
    except CpfFormatError as e:
        return {'error': str(e)}, HTTPStatus.BAD_REQUEST

    except RequestError as e:
        return {'error': str(e)}

    except KeysFormatError as e:
        return {'error': str(e)}, HTTPStatus.BAD_REQUEST