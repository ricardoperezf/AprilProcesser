count = 0
vector_verb = []


def splitter():
    with open('Ortega Y Gasset, José - El Sentido Histórico De La Teoría De Einstein.txt', 'r') as f:
        for line in f:
            get_text_file(line)


def get_text_file(word):
    words_separate = split_sentences(word)
    # vector.append(output)
    # print(salida)
    print(words_separate)


def split_sentences(output):
    for word in output.split():
        if "," in word:
            new_word = word.replace(',', '')
            finder_of_verbs = find_verb(new_word)
        else:
            finder_of_verbs = find_verb(word)


def find_verb(palabra):
    global count
    with open('verbos.txt', 'r') as f:
        for line in f:
            for word in line.split():
                if palabra == word:
                    count += 1
                    print("\n\nSE ENCONTRO EL VERBO = " + word + " Y LA PALABRA FUE = " + palabra + "\n\n" + " COUNT = " + str(count_verbs))
                    vector_verb.append(count)
                    return "Se encontró un verbo"
splitter()
