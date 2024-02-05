import azure.functions as func

from engine.additional_functions import bp
from api.app import app as fastapi_app

app = func.AsgiFunctionApp(app=fastapi_app, http_auth_level=func.AuthLevel.ANONYMOUS)
app.register_functions(bp)
