from flask import Flask

from flask_cors import CORS
from dotenv import load_dotenv

from .example.example import example

load_dotenv()

application = Flask(__name__)

application.register_blueprint(example)
cors = CORS(application)
