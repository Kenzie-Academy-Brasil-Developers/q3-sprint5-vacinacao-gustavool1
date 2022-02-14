from http.client import BAD_REQUEST
from app.exceptions.NotAstringError import NotAstringError
from app.models.person_vaccined_model import PersonVaccined
from flask import jsonify, request, current_app
from http import HTTPStatus
from datetime import datetime, timedelta
from sqlalchemy.exc import IntegrityError, DataError
from app.models.person_vaccined_model import PersonVaccined
def create_vaccined_person():
    try: 
        necessarie_keys = ["cpf", "name", "vaccine_name", "health_unit_name"]
        data = request.get_json()

        for value in data.values():
            if not type(value) is str:
                raise NotAstringError 

        for character in data["cpf"]:
            if character not in ["0","1","2","3","4","5","6","7","8","9"]:
                return {"msg":"CPF field allows only number"}, HTTPStatus.BAD_REQUEST 

        data["name"] = data["name"].upper()
        data["vaccine_name"] = data["vaccine_name"].upper()
        data["health_unit_name"] = data["health_unit_name"].upper()

        
        new_person_vaccined = PersonVaccined(**data)
        current_app.db.session.add(new_person_vaccined)
        current_app.db.session.commit()

        return jsonify(new_person_vaccined), HTTPStatus.CREATED

    except  NotAstringError : 
        return {"msg":"All the fields on the body must be strings"}, HTTPStatus.BAD_REQUEST

    except KeyError:
        return {"msg": "Your body request is missing one or more of the following keys -> cpf, name, vaccine_name, health_unit_name"},  HTTPStatus.BAD_REQUEST

    except IntegrityError:
        return {"msg": "This CPF already exists on the database"},  HTTPStatus.CONFLICT
    
    except DataError:
        return {"msg":"CPF field should have 11 digits"}, HTTPStatus.BAD_REQUEST




def get_vaccined_list():

    vaccined_persons = (PersonVaccined.query.all())
    vaccined_persons = [
        { 
            "cpf":person.cpf,
            "name":person.name,
            "first_shot_date":person.first_shot_date,
            "second_shot_date":person.second_shot_date,
            "vaccine_name": person.vaccine_name,
            "health_unit_name":person.health_unit_name
        } for person in vaccined_persons
    ]
    print(vaccined_persons)
    return jsonify(vaccined_persons)