import connexion

from openapi_server import encoder


app = connexion.App(__name__, specification_dir='./openapi/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('openapi.yaml',
            arguments={'title': 'Simple Customer API'},
            pythonic_params=True)

application = app.app
