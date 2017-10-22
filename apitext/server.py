from flask import Flask, request, jsonify
########################################################################################################################

app = Flask(__name__)
vector = []
vector_verbos = []
cantidad = 0

########################################################################################################################


@app.route('/api/v1', methods=['POST', 'GET'])
def get_param():
    global vector
    global vector_verbos
    if request.method == "POST":
        p = request.args
        salida = p['ejemplo']
        vector.append(salida)
        #print(salida)
        find_verb(salida)
        return "ENVIANDO"
    else:
        return jsonify(vector_verbos)

def find_verb(palabra):
    global cantidad
    global vector_verbos
    with open('verbos.txt', 'r') as f:
        for line in f:
            for word in line.split():
                if palabra == word:
                    cantidad += 1
                    print("\n\nSE ENCONTRÓ EL VERBO = " + word + " Y LA PALABRA FUE = " + palabra + "\n\n")
                    print(str(cantidad))
                    vector_verbos.append(cantidad)
                    return cantidad


########################################################################################################################
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")