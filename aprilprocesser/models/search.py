class Search:
    def __init__(self, text_file):
        self.text_file = text_file
        self.vector = []
        self.count_verbs = 0
        self.count_nouns = 0
        self.count_pronouns = 0
        self.count_adjective = 0
        self.count_another_word = 0
        self.count_total_words = 0
        self.verb_text_file = ""
        self.noun_text_file = ""
        self.adjective_text_file = ""
        self.pronoun_text_file = ""

    def split_sentences(self):
        output = self.text_file
        for word in output.split():
            self.count_total_words += 1
            if "," in word:
                new_word = word.replace(',', '')
                new_word_lower = new_word.lower()
                self.find_first_letter(new_word_lower)
            elif "." in word:
                new_word = word.replace(".", "")
                new_word_lower = new_word.lower()
                self.find_first_letter(new_word_lower)
            elif ";" in word:
                new_word = word.replace(";", "")
                new_word_lower = new_word.lower()
                self.find_first_letter(new_word_lower)
            elif "!" in word:
                new_word = word.replace("!", "")
                new_word_lower = new_word.lower()
                self.find_first_letter(new_word_lower)
            elif "?" in word:
                new_word = word.replace("?", "")
                new_word_lower = new_word.lower()
                self.find_first_letter(new_word_lower)
            elif "¿" in word:
                new_word = word.replace("¿", "")
                new_word_lower = new_word.lower()
                self.find_first_letter(new_word_lower)
            elif "-" in word:
                new_word = word.replace("-", "")
                new_word_lower = new_word.lower()
                self.find_first_letter(new_word_lower)
            elif "(" in word:
                new_word = word.replace("(", "")
                new_word_lower = new_word.lower()
                self.find_first_letter(new_word_lower)
            elif ")" in word:
                new_word = word.replace(")", "")
                new_word_lower = new_word.lower()
                self.find_first_letter(new_word_lower)
            else:
                new_word_lower = word.lower()
                self.find_first_letter(new_word_lower)
        return "Terminado"

    def find_first_letter(self, the_word):
        if the_word[0] == "a" or the_word[0] == "b" or the_word[0] == "c" or the_word[0] == "d" or the_word[0] == "e":
            self.verb_text_file = "books/verbos/verbos_abcde.txt"
            self.noun_text_file = "books/sustantivos/sustantivos_abcde.txt"
            self.adjective_text_file = "books/adjetivos/adjetivos_abcde.txt"
            self.pronoun_text_file = "books/pronombres/pronombres_abcde.txt"
            return self.finder_brain(the_word)
        elif the_word[0] == "f" or the_word[0] == "g" or the_word[0] == "h" or the_word[0] == "i" or the_word[0] == "j":
            self.verb_text_file = "books/verbos/verbos_fghij.txt"
            self.noun_text_file = "books/sustantivos/sustantivos_fghij.txt"
            self.adjective_text_file = "books/adjetivos/adjetivos_fghij.txt"
            self.pronoun_text_file = "books/pronombres/pronombres_fghij.txt"
            return self.finder_brain(the_word)
        elif the_word[0] == "k" or the_word[0] == "l" or the_word[0] == "m" or the_word[0] == "n" or the_word[0] == "o":
            self.verb_text_file = "books/verbos/verbos_klmno.txt"
            self.noun_text_file = "books/sustantivos/sustantivos_klmno.txt"
            self.adjective_text_file = "books/adjetivos/adjetivos_klmno.txt"
            self.pronoun_text_file = "books/pronombres/pronombres_klmno.txt"
            return self.finder_brain(the_word)
        elif the_word[0] == "p" or the_word[0] == "q" or the_word[0] == "r" or the_word[0] == "s" or the_word[0] == "t":
            self.verb_text_file = "books/verbos/verbos_pqrst.txt"
            self.noun_text_file = "books/sustantivos/sustantivos_pqrst.txt"
            self.adjective_text_file = "books/adjetivos/adjetivos_pqrst.txt"
            self.pronoun_text_file = "books/pronombres/pronombres_pqrst.txt"
            return self.finder_brain(the_word)
        elif the_word[0] == "u" or the_word[0] == "v" or the_word[0] == "w" or the_word[0] == "x" or the_word[
            0] == "y" or the_word[0] == "z":
            self.verb_text_file = "books/verbos/verbos_uvwxyz.txt"
            self.noun_text_file = "books/sustantivos/sustantivos_uvwxyz.txt"
            self.adjective_text_file = "books/adjetivos/adjetivos_uvwxyz.txt"
            self.pronoun_text_file = "books/pronombres/pronombres_uwxyz.txt"
            return self.finder_brain(the_word)

    def finder_brain(self, word):
        finder_of_verb = self.find_verb(word)
        finder_of_noun = self.find_noun(word)
        finder_of_adjective = self.find_adjective(word)
        finder_of_pronoun = self.find_pronoun(word)
        if finder_of_verb != "Se encontro" and finder_of_noun != "Se encontro" and finder_of_adjective != "Se encontro" and finder_of_pronoun != "Se encontro":
            self.count_another_word += 1
        return self.count_another_word

    def find_verb(self, word_parameter):
        with open(self.verb_text_file, 'r') as f:
            for line in f:
                for word in line.split():
                    if word_parameter == word.lower():
                        self.count_verbs += 1
                        return "It founded"

    def find_noun(self, word_parameter):
        with open(self.noun_text_file, 'r') as f:
            for line in f:
                for word in line.split():
                    if word_parameter == word.lower():
                        self.count_nouns += 1
                        return "It founded"

    def find_adjective(self, word_parameter):
        with open(self.adjective_text_file, 'r') as f:
            for line in f:
                for word in line.split():
                    if word_parameter == word.lower():
                        self.count_adjective += 1
                        return "It founded"

    def find_pronoun(self, word_parameter):
        with open(self.pronoun_text_file, 'r') as f:
            for line in f:
                for word in line.split():
                    if word_parameter == word.lower():
                        self.count_pronouns += 1
                        return "Se encontro"

    def get_total_count(self):
        self.vector.append({'verbs': self.count_verbs})
        self.vector.append({'nouns': self.count_nouns})
        self.vector.append({'adjectives': self.count_adjective})
        self.vector.append({'pronouns': self.count_pronouns})
        self.vector.append({'another_words': self.count_another_word})
        self.vector.append({'total_words': self.count_total_words})
        return self.vector