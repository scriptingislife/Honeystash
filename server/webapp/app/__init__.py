from flask_bootstrap import Bootstrap
from flask import Flask

app = Flask(__name__)
Bootstrap(app)

from app import main
