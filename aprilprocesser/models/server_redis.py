from flask import Flask, request, jsonify
import redis

########################################################################################################################
# VARIABLES QUE SERVIRÁN PARA USARLAS EN DISTINTOS ALGORITMOS

r = redis.StrictRedis('localhost')

verb_list_redis = []
noun_list_redis = []
adjective_list_redis = []
pronoun_list_redis = []
rest_list_redis = []

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
    global vector, count_verbs, count_nouns, count_adjective, count_pronouns, count_another_word, count_total_words, adjective_text_file, pronoun_text_file
    if request.method == "POST":
        output = request.form['ejemplo']
        split_sentences(output)
        return jsonify("SERVIDOR = Se termino de hacer el procesamiento de texto ...")
    else:
        vector.append(str(count_verbs))
        vector.append(str(count_nouns))
        vector.append(str(count_adjective))
        vector.append(str(count_pronouns))
        vector.append(str(count_another_word))
        vector.append(str(count_total_words))
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
        elif "!" in word:
            new_word = word.replace("!", "")
            find_first_letter(new_word.lower())
        elif "?" in word:
            new_word = word.replace("?", "")
            find_first_letter(new_word.lower())
        elif "¿" in word:
            new_word = word.replace("¿", "")
            find_first_letter(new_word.lower())
        elif "-" in word:
            new_word = word.replace("-", "")
            find_first_letter(new_word.lower())
        elif "(" in word:
            new_word = word.replace("(", "")
            find_first_letter(new_word.lower())
        elif ")" in word:
            new_word = word.replace(")", "")
            find_first_letter(new_word.lower())
        else:
            find_first_letter(word.lower())


# MÉTODO QUE PERMITE CONOCER LA PRIMERA LETRA DE UNA PALABRA PARA ASÍ SABER A CUAL ARCHIVO ANALIZAR SU TIPO DE PALABRA
#   QUE CORRESPONDE.
def find_first_letter(palabra):
    global verb_text_file, verb_list_redis, noun_text_file, noun_list_redis, adjective_text_file, adjective_list_redis, pronoun_text_file, pronoun_list_redis
    if palabra[0] == "a" or palabra[0] == "b" or palabra[0] == "c" or palabra[0] == "d" or palabra[0] == "e":
        verb_text_file = "verbs/verbos_abcde.txt"
        verb_list_redis = "v_abcde"
        noun_text_file = "nouns/sustantivos_abcde.txt"
        noun_list_redis = "n_abcde"
        adjective_text_file = "adjectives/adjetivos_abcde.txt"
        adjective_list_redis = "a_abcde"
        pronoun_text_file = "pronouns/pronombres_abcde.txt"
        pronoun_list_redis = "p_abcde"
        finder(palabra)
    elif palabra[0] == "f" or palabra[0] == "g" or palabra[0] == "h" or palabra[0] == "i" or palabra[0] == "j":
        verb_text_file = "verbs/verbos_fghij.txt"
        verb_list_redis = "v_fghij"
        noun_text_file = "nouns/sustantivos_fghij.txt"
        noun_list_redis = "n_fghij"
        adjective_text_file = "adjectives/adjetivos_fghij.txt"
        adjective_list_redis = "a_fghij"
        pronoun_text_file = "pronouns/pronombres_fghij.txt"
        pronoun_list_redis = "p_fghij"
        finder(palabra)
    elif palabra[0] == "k" or palabra[0] == "l" or palabra[0] == "m" or palabra[0] == "n" or palabra[0] == "o":
        verb_text_file = "verbs/verbos_klmno.txt"
        verb_list_redis = "v_klmno"
        noun_text_file = "nouns/sustantivos_klmno.txt"
        noun_list_redis = "n_klmno"
        adjective_text_file = "adjectives/adjetivos_klmno.txt"
        adjective_list_redis = "a_klmno"
        pronoun_text_file = "pronouns/pronombres_klmno.txt"
        pronoun_list_redis = "p_klmno"
        finder(palabra)
    elif palabra[0] == "p" or palabra[0] == "q" or palabra[0] == "r" or palabra[0] == "s" or palabra[0] == "t":
        verb_text_file = "verbs/verbos_pqrst.txt"
        verb_list_redis = "v_pqrst"
        noun_text_file = "nouns/sustantivos_pqrst.txt"
        noun_list_redis = "n_pqrst"
        adjective_text_file = "adjectives/adjetivos_pqrst.txt"
        adjective_list_redis = "a_pqrst"
        pronoun_text_file = "pronouns/pronombres_pqrst.txt"
        pronoun_list_redis = "p_pqrst"
        finder(palabra)
    elif palabra[0] == "u" or palabra[0] == "v" or palabra[0] == "w" or palabra[0] == "x" or palabra[0] == "y" or \
                    palabra[0] == "z":
        verb_text_file = "verbs/verbos_uvwxyz.txt"
        verb_list_redis = "v_uwxyz"
        noun_text_file = "nouns/sustantivos_uvwxyz.txt"
        noun_list_redis = "n_uwxyz"
        adjective_text_file = "adjectives/adjetivos_uvwxyz.txt"
        adjective_list_redis = "a_uwxyz"
        pronoun_text_file = "pronouns/pronombres_uvwxyz.txt"
        pronoun_list_redis = "p_uwxyz"
        finder(palabra)


# MÉTODO QUE PERMITE HACER LOS DISTINTOS LLAMADOS DE CADA TIPO DE PALABRA PARA HACER EL ANÁLISIS COMPARATIVO
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
    global count_verbs, vector, verb_text_file, verb_list_redis
    verb_redis = r.lrange(verb_list_redis, 0, -1)
    if str(verb_redis) == "[]":
        with open(verb_text_file, 'r') as f:
            for line in f:
                for word in line.split():
                    r.lpush(verb_list_redis, word)
    else:
        for word in verb_redis:
            if "b'" in str(word):
                new_word = str(word).replace("b'", "")
            if "'" in new_word:
                new_word = str(new_word).replace("'", "")
            if palabra == new_word:
                count_verbs += 1
                return "Se encontro"


# MÉTODO QUE PERMITE HACER EL ANÁLISIS COMPARATIVO ENTRE LAS PALABRAS RECIBIDAD DEL TXT FILE CON LAS PALABRAS DEL TXT
#   INTERNO DE NOUNS.
def find_noun(palabra):
    global count_nouns, vector, noun_text_file, noun_list_redis
    noun_redis = r.lrange(noun_list_redis, 0, -1)
    if str(noun_redis) == "[]":
        with open(noun_text_file, 'r') as f:
            for line in f:
                for word in line.split():
                    r.lpush(noun_list_redis, word)
    else:
        for word in noun_redis:
            if "b'" in str(word):
                new_word = str(word).replace("b'", "")
            if "'" in new_word:
                new_word = str(new_word).replace("'", "")
            if palabra == new_word:
                count_nouns += 1
                return "Se encontro"


# MÉTODO QUE PERMITE HACER EL ANÁLISIS COMPARATIVO ENTRE LAS PALABRAS RECIBIDAD DEL TXT FILE CON LAS PALABRAS DEL TXT
#   INTERNO DE ADJECTIVES.
def find_adjective(palabra):
    global count_adjective, vector, adjective_text_file, adjective_list_redis
    adjective_redis = r.lrange(adjective_list_redis, 0, -1)
    if str(adjective_redis) == "[]":
        with open(adjective_text_file, 'r') as f:
            for line in f:
                for word in line.split():
                    r.lpush(adjective_list_redis, word)
    else:
        for word in adjective_redis:
            if "b'" in str(word):
                new_word = str(word).replace("b'", "")
            if "'" in new_word:
                new_word = str(new_word).replace("'", "")
            if palabra == new_word:
                count_adjective += 1
                return "Se encontro"


# MÉTODO QUE PERMITE HACER EL ANÁLISIS COMPARATIVO ENTRE LAS PALABRAS RECIBIDAD DEL TXT FILE CON LAS PALABRAS DEL TXT
#   INTERNO DE PRONOUNS.
def find_pronoun(palabra):
    global count_pronouns, vector, pronoun_text_file, pronoun_list_redis
    pronoun_redis = r.lrange(pronoun_list_redis, 0, -1)
    if str(pronoun_redis) == "[]":
        with open(pronoun_text_file, 'r') as f:
            for line in f:
                for word in line.split():
                    r.lpush(pronoun_list_redis, word)
    else:
        for word in pronoun_redis:
            if "b'" in str(word):
                new_word = str(word).replace("b'", "")
            if "'" in new_word:
                new_word = str(new_word).replace("'", "")
            if palabra == new_word:
                count_pronouns += 1
                return "Se encontro"
