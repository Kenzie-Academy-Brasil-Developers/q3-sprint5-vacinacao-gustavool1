from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime, timedelta
@dataclass
class PersonVaccined(db.Model):
    cpf: str
    name:str
    first_shot_date:str
    second_shot_date:str
    vaccine_name:str
    health_unit_name:str
    
    __tablename__ = "vaccine_cards"
    cpf = Column(String(11), primary_key=True, unique=True)
    name = Column(String(60), nullable=False)
    first_shot_date = Column(DateTime, default=str(datetime.now().strftime("%d/%m/%Y %H:%M")))
    second_shot_date = Column(DateTime, default=str(datetime.today() + timedelta(days=+90)))
    vaccine_name = Column(String(50), nullable=False)
    health_unit_name = Column(String(50))