from flask import Flask, jsonify
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "entrenamiento.settings")
django.setup()

from user.models import User

app = Flask(__name__)



