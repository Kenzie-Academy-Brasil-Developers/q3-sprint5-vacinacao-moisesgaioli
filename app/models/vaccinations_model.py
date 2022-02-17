from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import validates
from datetime import datetime, timedelta
from dataclasses import dataclass
from app.configs.database import db
from app.models.exc import CpfFormatError, KeyFoundError, KeysFormatError, RequestError


@dataclass
class VaccineCards(db.Model):
    __tablename__ = "vaccine_cards"

    date_second_shot = datetime.now() + timedelta(days=90)

    cpf: str
    name: str
    first_shot_date: str
    second_shot_date: str
    vaccine_name: str
    health_unit_name: str


    cpf = Column(String, primary_key=True, unique=True)
    name = Column(String, nullable=False)
    first_shot_date = Column(DateTime, default=datetime.now)
    second_shot_date = Column(DateTime, default=date_second_shot)
    vaccine_name = Column(String, nullable=False)
    health_unit_name = Column(String)

    @validates('cpf', 'name', 'vaccine_name', 'health_unit_name')
    def validate_fields(self, key, value):

        if type(value) != str:
            raise KeysFormatError('All keys should be `string`.')

        if key == 'cpf' and len(value) != 11:
            raise CpfFormatError('Key `cpf` should contains 11 characteres.')


        return value.title()