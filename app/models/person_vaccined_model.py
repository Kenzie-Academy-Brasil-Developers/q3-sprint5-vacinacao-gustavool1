from app.configs.database import db
from sqlalchemy import Column, Integer, String, Float, DateTime
class PersonVaccined(db.Model):
    __tablename__ = "vaccine_cards"
    cpf = Column(String(11), primary_key=True, unique=True)
    name = Column(String(60), nullable=False)
    first_shot_date = Column(DateTime)
    second_shot_date = Column(DateTime)
    vaccine_name = Column(String(50), nullable=False)
    health_unit_name = Column(String(50))