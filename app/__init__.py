from flask_swagger_ui import get_swaggerui_blueprint
from flask import Flask
from sqlalchemy import create_engine, MetaData

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

# swagger specific #
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yaml'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "GENE-SEARCH-REST-API"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
# end swagger specific #
connection = 'mysql://'+app.config['USER']+'@'+app.config['HOST']+':'+app.config['PORT']+'/'+app.config['DATABASE']
engine = create_engine(connection)
metadata = MetaData(bind=engine)
from app import views
