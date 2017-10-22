from flask import Flask, request, jsonify

########################################################################################################################

app = Flask(__name__)
vector = []
vector_verb = []
count_verbs = 0
count_nouns = 0
count_total_words = 0

########################################################################################################################

@app.route('/api/v1', methods=['POST', 'GET'])
def get_text_file():
    global vector
    global vector_verb
    global count_verbs
    global count_nouns
    global count_total_words

    if request.method == "POST":
        request_post = request.args
        output = request_post['ejemplo']
        words_separate = split_sentences(output)
        # vector.append(output)
        # print(salida)
        return jsonify(words_separate)
    else:
        vector_verb.append("Verbos: " + str(count_verbs))
        vector_verb.append("Sustantivos: " + str(count_nouns))
        vector_verb.append("Total palabras: " + str(count_total_words))
        return jsonify(vector_verb)


def split_sentences(output):
    global count_total_words
    for word in output.split():
        count_total_words += 1
        if "," in word:
            new_word = word.replace(',', '')
            find_verb(new_word)
            find_noun(new_word)
        else:
            find_verb(word)
            find_noun(word)

def find_verb(palabra):
    global count_verbs
    global vector_verb
    with open('verbos.txt', 'r') as f:
        for line in f:
            for word in line.split():
                if palabra == word:
                    count_verbs += 1
                    print("\n\nSE ENCONTRO EL VERBO = " + word + " Y LA PALABRA FUE = " + palabra + "\n\n" + " COUNT = " + str(count_verbs))
                    #new_index = "Se encontro = " + palabra + " count = " + str(count_verbs)
                    #vector_verb.append(new_index)
                    return "Se encontró un verbo"

def find_noun(palabra):
    global count_nouns
    global vector_verb
    with open('sustantivos.txt', 'r') as f:
        for line in f:
            for word in line.split():
                if palabra == word:
                    count_nouns += 1
                    print(
                        "\n\nSE ENCONTRO EL SUSTANTIVO = " + word + " Y LA PALABRA FUE = " + palabra + "\n\n" + " COUNT = " + str(
                            count_nouns))
                    # new_index = "Se encontro el sustantivo = " + palabra + " count = " + str(count_nouns)
                    # vector_verb.append(new_index)
                    return "Se encontró un sustantivo"
########################################################################################################################
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
