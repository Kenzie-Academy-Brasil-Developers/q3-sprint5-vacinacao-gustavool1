from app.exceptions.MissingFieldError import MissingFieldError
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
        print('testtttt', all(item in necessarie_keys for item in data.keys()))
        if all(item in necessarie_keys for item in data.keys()):
            raise MissingFieldError

        for value in data.values():
            if not type(value) is str:
                raise NotAstringError 

        data["name"] = data["name"].title()
        data["vaccine_name"] = data["vaccine_name"].title()
        data["health_unit_name"] = data["health_unit_name"].title()

        data["first_shot_date"] = str(datetime.now().strftime("%d/%m/%Y %H:%M"))
        second_shot_date = datetime.today() + timedelta(days=+90)
        data["second_shot_date"] = str(second_shot_date.strftime("%d/%m/%Y %H:%M"))
        new_person_vaccined = {
            "cpf":data["cpf"],
            "name":data["name"], 
            "vaccine_name":data["vaccine_name"],
            "health_unit_name":data["health_unit_name"],
            "first_shot_date":data["first_shot_date"],
            "second_shot_date":data["second_shot_date"] 
        }
        new_person_vaccined = PersonVaccined(**new_person_vaccined)
        current_app.db.session.add(new_person_vaccined)
        current_app.db.session.commit()
        print(new_person_vaccined)

        return{
            "cpf":new_person_vaccined.cpf,
            "name":new_person_vaccined.name,
            "first_shot_date":new_person_vaccined.first_shot_date,
            "second_shot_date":new_person_vaccined.second_shot_date,
            "vaccine_name": new_person_vaccined.vaccine_name,
            "health_unit_name":new_person_vaccined.health_unit_name
        }, HTTPStatus.CREATED

    except  NotAstringError : 
        return {"msg":"All the fields on the body must be strings"}, HTTPStatus.BAD_REQUEST

    except MissingFieldError:
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