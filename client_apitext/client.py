import requests
import time

def index(word):
     post_request = requests.post('http://192.168.0.15:5000/api/v1?ejemplo=' + str(word))
     print(post_request.text)

def splitter():
    with open('Ortega Y Gasset, José - El Sentido Histórico De La Teoría De Einstein.txt', 'r') as f:
        for line in f:
            index(line)
splitter()