from flask import Blueprint

from app.controllers.vaccinations_controller import create_vaccined_person, get_vaccined_list
bp = Blueprint("", __name__, url_prefix="/vaccinations")

bp.post("")(create_vaccined_person)
bp.get("")(get_vaccined_list)