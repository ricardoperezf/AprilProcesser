#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS

aprilprocesser_app = Flask(__name__)
aprilprocesser_app.config['MONGO_DBNAME'] = "reportcard"
aprilprocesser_app.config['MONGO_URI'] = "mongodb://ricardo:ricardomongodb@ds163826.mlab.com:63826/reportcard"

mongo = PyMongo(aprilprocesser_app)

CORS(aprilprocesser_app)

from aprilprocesser.endpoints import *
