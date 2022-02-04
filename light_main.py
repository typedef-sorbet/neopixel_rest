import connexion
from swagger_server import encoder

options = {"swagger_ui": False}
app = connexion.App(__name__, specification_dir='./swagger_server/swagger/', options=options)
app.add_api("swagger.yaml", arguments={'title': "Light API"}, pythonic_params=True)
app.app.json_encoder = encoder.JSONEncoder

# Exposing WSGI callable to uWSGI
application = app.app

if __name__ == "__main__":
    app.run(port=8080)
