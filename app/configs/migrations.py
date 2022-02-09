from flask_migrate import Migrate

def init_app(app):

    from app.models.person_vaccined_model import PersonVaccined
    
    Migrate(app, app.db)