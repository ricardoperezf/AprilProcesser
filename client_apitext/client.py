from flask import Flask, render_template
import requests
import json

########################################################################################################################

app = Flask(__name__)


########################################################################################################################

#   MÉTODO QUE PERMITE MEDIANTE LA RUTA DE /START HACER EL POST AL SERVIDOR
@app.route('/start')
def post_server():
    libro = open('Ortega Y Gasset, José - El Sentido Histórico De La Teoría De Einstein.txt', 'r')
    word = libro.read()
    post_request = requests.post('http://192.168.1.16:5000/api/v1', data={"ejemplo": str(word)})
    return render_template('./index.html', resultado=json.dumps(post_request.text))


#   MÉTODO QUE PERMITE MEDIANTE LA RUTA DE /RESULTADO VER EL PROCESAMIENTO DEL TXT FILE.
@app.route('/resultado')
def get_final_result():
    theRequest = requests.get('http://192.168.1.16:5000/api/v1')
    return render_template('./index_result.html', resultado=json.dumps(theRequest.text))


########################################################################################################################
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
