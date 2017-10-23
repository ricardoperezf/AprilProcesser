from flask import Flask, request, jsonify

########################################################################################################################
# VARIABLES QUE SERVIRÁN PARA USARLAS EN DISTINTOS ALGORITMOS
app = Flask(__name__)
vector = []
count_verbs = 0
count_nouns = 0
count_adjective = 0
count_pronouns = 0
count_another_word = 0
count_total_words = 0


########################################################################################################################
#   MÉTODOS POST QUE PERMITIRÁ RECIBIR EL TXT FILE
#   MÉTODO GET QUE PERMITIRÁ ENVIAR LOS RESULTADOS DEL CONTEO DE VERBOS, SUSTANTIVOS, ADJETIVOS, PRONOMBRES Y EL RESTO

@app.route('/api/v1', methods=['POST', 'GET'])
def get_text_file():
    global vector
    global count_verbs
    global count_nouns
    global count_adjective
    global count_pronouns
    global count_another_word
    global count_total_words

    if request.method == "POST":
        request_post = request.args
        output = request_post['ejemplo']
        split_sentences(output)
        return jsonify("SERVIDOR = Recibiendo txt file del cliente...")
    else:
        vector.append("Verbos: " + str(count_verbs))
        vector.append("Sustantivos: " + str(count_nouns))
        vector.append("Adjetivos: " + str(count_adjective))
        vector.append("Pronombres: " + str(count_pronouns))
        vector.append("Resto: " + str(count_another_word))
        vector.append("Total palabras: " + str(count_total_words))
        return jsonify(vector)


########################################################################################################################
#   MÉTODO QUE PERMITE HACER SPLIT A CADA LINEA QUE LLEGA DE UN CLIENTE Y SEPARARLA EN PALABRAS.
#   LUEGO PERMITRÁ HACER LLAMADOS AL MÉTODO QUE HACE PIVOT A LOS MÉTODOS DE PALABRAS.

def split_sentences(output):
    global count_total_words
    for word in output.split():
        count_total_words += 1
        if "," in word:
            new_word = word.replace(',', '')
            finder(new_word)
        elif "." in word:
            new_word = word.replace(".", "")
            finder(new_word)
        else:
            finder(word)


# MÉTODO QUE PERMITE HACER LOS DISTINTOS LLAMADOS DE CADA TIPO DE PALABRA PARA HACER EL ANÁLISIS COMPARATIVO
#   DE LOS MÉTODOS DE BUSCAR VERBO, SUSTANTIVO, ADJETIVO, PRONOMBRE.
def finder(word):
    global count_another_word
    finder_of_verb = find_verb(word)
    finder_of_noun = find_noun(word)
    finder_of_adjective = find_adjective(word)
    finder_of_pronoun = find_pronoun(word)
    if finder_of_verb != "Se encontro" and finder_of_noun != "Se encontro" and finder_of_adjective != "Se encontro" and finder_of_pronoun != "Se encontro":
        count_another_word += 1


# MÉTODO QUE PERMITE HACER EL ANÁLISIS COMPARATIVO ENTRE LAS PALABRAS RECIBIDAD DEL TXT FILE CON LAS PALABRAS DEL TXT
#   INTERNO DE VERBS.
def find_verb(palabra):
    global count_verbs
    global vector
    with open('verbos.txt', 'r') as f:
        for line in f:
            for word in line.split():
                if palabra == word:
                    count_verbs += 1
                    # print("\n\nSE ENCONTRO EL VERBO = " + word + " Y LA PALABRA FUE = " + palabra + "\n\n" + " COUNT = " + str(count_verbs))
                    # new_index = "Se encontro = " + palabra + " count = " + str(count_verbs)
                    # vector_verb.append(new_index)
                    return "Se encontro"


# MÉTODO QUE PERMITE HACER EL ANÁLISIS COMPARATIVO ENTRE LAS PALABRAS RECIBIDAD DEL TXT FILE CON LAS PALABRAS DEL TXT
#   INTERNO DE NOUNS.
def find_noun(palabra):
    global count_nouns
    global vector
    with open('sustantivos.txt', 'r') as f:
        for line in f:
            for word in line.split():
                if palabra == word:
                    count_nouns += 1
                    # print("\n\nSE ENCONTRO EL SUSTANTIVO = " + word + " Y LA PALABRA FUE = " + palabra + "\n\n" + " COUNT = " + str(count_nouns))
                    # new_index = "Se encontro el sustantivo = " + palabra + " count = " + str(count_nouns)
                    # vector_verb.append(new_index)
                    return "Se encontro"


# MÉTODO QUE PERMITE HACER EL ANÁLISIS COMPARATIVO ENTRE LAS PALABRAS RECIBIDAD DEL TXT FILE CON LAS PALABRAS DEL TXT
#   INTERNO DE ADJECTIVES.
def find_adjective(palabra):
    global count_adjective
    global vector
    with open('adjetivos.txt', 'r') as f:
        for line in f:
            for word in line.split():
                if palabra == word:
                    count_adjective += 1
                    # print("\n\nSE ENCONTRO EL ADJETIVO = " + word + " Y LA PALABRA FUE = " + palabra + "\n\n" + " COUNT = " + str(count_adjective))
                    # new_index = "Se encontro = " + palabra + " count = " + str(count_adjective)
                    # vector.append(new_index)
                    return "Se encontro"


# MÉTODO QUE PERMITE HACER EL ANÁLISIS COMPARATIVO ENTRE LAS PALABRAS RECIBIDAD DEL TXT FILE CON LAS PALABRAS DEL TXT
#   INTERNO DE PRONOUNS.
def find_pronoun(palabra):
    global count_pronouns
    global vector
    with open('pronombres.txt', 'r') as f:
        for line in f:
            for word in line.split():
                if palabra == word:
                    count_pronouns += 1
                    # print("\n\nSE ENCONTRO EL PRONOMBRE = " + word + " Y LA PALABRA FUE = " + palabra + "\n\n" + " COUNT = " + str(count_pronouns))
                    # new_index = "Se encontro = " + palabra + " count = " + str(count_verbs)
                    # vector.append(new_index)
                    return "Se encontro"


########################################################################################################################
#   INICIAR EL SERVIDOR EN LA DIRECCIÓN ESPECÍFICA Y PUERTO.
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
