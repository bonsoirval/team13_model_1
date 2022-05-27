from flask import Flask

app = Flask(__name__)

from team13_model import routes
