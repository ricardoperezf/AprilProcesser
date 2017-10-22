def libro():
    with open('Ortega Y Gasset, José - El Sentido Histórico De La Teoría De Einstein.txt', 'r') as f:
        for line in f:
            for word in line.split():
                if "," in word:
                    # print("REEMPLAZA ESTA PALABRA = " + word)
                    newWord = word.replace(',', '')
                    # print("SE REEMPLAZÓ POR = " + newWord)
                    # print(newWord)
                    search(newWord)
                else:
                    # print(word)
                    search(word)


cantidad = 0


def search(palabra):
    global cantidad
    with open('verbos.txt', 'r') as f:
        for line in f:
            for word in line.split():
                if palabra == word:
                    cantidad += 1
                    print("SE ENCONTRÓ EL VERBO = " + word + " Y LA PALABRA FUE = " + palabra)
                    print(str(cantidad))


libro()
