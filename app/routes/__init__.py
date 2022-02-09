from app.routes.vaccinations_route import bp as bp_vaccined

def init_app(app):
    app.register_blueprint(bp_vaccined)