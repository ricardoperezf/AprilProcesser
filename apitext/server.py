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
verb_text_file = ""
noun_text_file = ""
adjective_text_file = ""
pronoun_text_file = ""

########################################################################################################################
#   MÉTODOS POST QUE PERMITIRÁ RECIBIR EL TXT FILE
#   MÉTODO GET QUE PERMITIRÁ ENVIAR LOS RESULTADOS DEL CONTEO DE VERBOS, SUSTANTIVOS, ADJETIVOS, PRONOMBRES Y EL RESTO

@app.route('/api/v1', methods=['POST', 'GET'])
def get_text_file():
    global vector, count_verbs, count_nouns, count_adjective, count_pronouns, count_another_word, count_total_words, \
        adjective_text_file, pronoun_text_file
    if request.method == "POST":
        output = request.form['ejemplo']
        split_sentences(output)
        return jsonify("SERVIDOR = Se termino de hacer el procesamiento de texto ...")
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
            find_first_letter(new_word.lower())
        elif "." in word:
            new_word = word.replace(".", "")
            find_first_letter(new_word.lower())
        elif ";" in word:
            new_word = word.replace(";", "")
            find_first_letter(new_word.lower())
        else:
            find_first_letter(word.lower())

# MÉTODO QUE PERMITE CONOCER LA PRIMERA LETRA DE UNA PALABRA PARA ASÍ SABER A CUAL ARCHIVO ANALIZAR SU TIPO DE PALABRA
#   QUE CORRESPONDE.
def find_first_letter(palabra):
    global verb_text_file, noun_text_file, adjective_text_file, pronoun_text_file
    if palabra[0] == "a" or palabra[0] == "b" or palabra[0] == "c" or palabra[0] == "d" or palabra[0] == "e":
        verb_text_file = "verbos/verbos_abcde.txt"
        noun_text_file = "sustantivos/sustantivos_abcde.txt"
        adjective_text_file = "adjetivos/adjetivos_abcde.txt"
        pronoun_text_file = "pronombres/pronombres_abcde.txt"
        finder(palabra)
    elif palabra[0] == "f" or palabra[0] == "g" or palabra[0] == "h" or palabra[0] == "i" or palabra[0] == "j":
        verb_text_file = "verbos/verbos_fghij.txt"
        noun_text_file = "sustantivos/sustantivos_fghij.txt"
        adjective_text_file = "adjetivos/adjetivos_fghij.txt"
        pronoun_text_file = "pronombres/pronombres_fghij.txt"
        finder(palabra)
    elif palabra[0] == "k" or palabra[0] == "l" or palabra[0] == "m" or palabra[0] == "n" or palabra[0] == "o":
        verb_text_file = "verbos/verbos_klmno.txt"
        noun_text_file = "sustantivos/sustantivos_klmno.txt"
        adjective_text_file = "adjetivos/adjetivos_klmno.txt"
        pronoun_text_file = "pronombres/pronombres_klmno.txt"
        finder(palabra)
    elif palabra[0] == "p" or palabra[0] == "q" or palabra[0] == "r" or palabra[0] == "s" or palabra[0] == "t":
        verb_text_file = "verbos/verbos_pqrst.txt"
        noun_text_file = "sustantivos/sustantivos_pqrst.txt"
        adjective_text_file = "adjetivos/adjetivos_pqrst.txt"
        pronoun_text_file = "pronombres/pronombres_pqrst.txt"
        finder(palabra)
    elif palabra[0] == "u" or palabra[0] == "v" or palabra[0] == "w" or palabra[0] == "x" or palabra[0] == "y" \
            or palabra[0] == "z":
        verb_text_file = "verbos/verbos_uvwxyz.txt"
        noun_text_file = "sustantivos/sustantivos_uvwxyz.txt"
        adjective_text_file = "adjetivos/adjetivos_uvwxyz.txt"
        pronoun_text_file = "pronombres/pronombres_uwxyz.txt"
        finder(palabra)

#   MÉTODO QUE PERMITE HACER LOS DISTINTOS LLAMADOS DE CADA TIPO DE PALABRA PARA HACER EL ANÁLISIS COMPARATIVO
#   DE LOS MÉTODOS DE BUSCAR VERBO, SUSTANTIVO, ADJETIVO, PRONOMBRE. SI UNA PALABRA NO CORRESPONDE A LAS ANTERIORES
#   ENTONCES SE CONTARÁ COMO DEL RESTO.
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
    global count_verbs, vector, verb_text_file
    with open(verb_text_file, 'r') as f:
        for line in f:
            for word in line.split():
                if palabra == word.lower():
                    count_verbs += 1
                    # print("\n\nSE ENCONTRO EL VERBO = " + word + " Y LA PALABRA FUE = " + palabra + "\n\n" + " COUNT = " + str(count_verbs))
                    #new_index = "Se encontro = " + palabra + " count = " + str(count_verbs)
                    #vector.append(new_index)
                    return "Se encontro"


# MÉTODO QUE PERMITE HACER EL ANÁLISIS COMPARATIVO ENTRE LAS PALABRAS RECIBIDAD DEL TXT FILE CON LAS PALABRAS DEL TXT
#   INTERNO DE NOUNS.
def find_noun(palabra):
    global count_nouns, vector, noun_text_file
    with open(noun_text_file, 'r') as f:
        for line in f:
            for word in line.split():
                if palabra == word.lower():
                    count_nouns += 1
                    # print("\n\nSE ENCONTRO EL SUSTANTIVO = " + word + " Y LA PALABRA FUE = " + palabra + "\n\n" + " COUNT = " + str(count_nouns))
                    #new_index = "Se encontro el sustantivo = " + palabra + " count = " + str(count_nouns)
                    #vector.append(new_index)
                    return "Se encontro"


# MÉTODO QUE PERMITE HACER EL ANÁLISIS COMPARATIVO ENTRE LAS PALABRAS RECIBIDAD DEL TXT FILE CON LAS PALABRAS DEL TXT
#   INTERNO DE ADJECTIVES.
def find_adjective(palabra):
    global count_adjective, vector, adjective_text_file
    with open(adjective_text_file, 'r') as f:
        for line in f:
            for word in line.split():
                if palabra == word.lower():
                    count_adjective += 1
                    # print("\n\nSE ENCONTRO EL ADJETIVO = " + word + " Y LA PALABRA FUE = " + palabra + "\n\n" + " COUNT = " + str(count_adjective))
                    #new_index = "Se encontro = " + palabra + " count = " + str(count_adjective)
                    #vector.append(new_index)
                    return "Se encontro"

#   MÉTODO QUE PERMITE HACER EL ANÁLISIS COMPARATIVO ENTRE LAS PALABRAS RECIBIDAD DEL TXT FILE CON LAS PALABRAS DEL TXT
#   INTERNO DE PRONOUNS.
def find_pronoun(palabra):
    global count_pronouns, vector, pronoun_text_file
    with open(pronoun_text_file, 'r') as f:
        for line in f:
            for word in line.split():
                if palabra == word.lower():
                    count_pronouns += 1
                    # print("\n\nSE ENCONTRO EL PRONOMBRE = " + word + " Y LA PALABRA FUE = " + palabra + "\n\n" + " COUNT = " + str(count_pronouns))
                    #new_index = "Se encontro = " + palabra + " count = " + str(count_verbs)
                    #vector.append(new_index)
                    return "Se encontro"


########################################################################################################################
#   INICIAR EL SERVIDOR EN LA DIRECCIÓN ESPECÍFICA Y PUERTO.
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")