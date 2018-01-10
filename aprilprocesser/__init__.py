#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS

aprilprocesser_app = Flask(__name__)
aprilprocesser_app.config['MONGO_DBNAME'] = "aprilprocesser"
aprilprocesser_app.config['MONGO_URI'] = "mongodb://ricardo:ricardomongodb@ds023495.mlab.com:23495/aprilprocesser"

mongo = PyMongo(aprilprocesser_app)

CORS(aprilprocesser_app)

from aprilprocesser.endpoints import *