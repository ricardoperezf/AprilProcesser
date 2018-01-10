class Search:
    def __init__(self, text_file):
        self.text_file = text_file
        self.vector = []
        self.count_verbs = 0
        self.count_nouns = 0
        self.count_pronouns = 0
        self.count_adjective = 0
        self.count_other_words = 0
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
                self.replace_word(",", word)
            elif "." in word:
                self.replace_word(".", word)
            elif ";" in word:
                self.replace_word(";", word)
            elif "!" in word:
                self.replace_word("!", word)
            elif "?" in word:
                self.replace_word("?", word)
            elif "¿" in word:
                self.replace_word("¿", word)
            elif "-" in word:
                self.replace_word("-", word)
            elif "(" in word:
                self.replace_word("(", word)
            elif ")" in word:
                self.replace_word(")", word)
            else:
                new_word_lower = word.lower()
                self.set_first_letter(new_word_lower)
        return self.get_result()

    def replace_word(self, sign, word):
        new_word = word.replace(sign, '')
        new_word_lower = new_word.lower()
        return self.set_first_letter(new_word_lower)

    def set_first_letter(self, the_word):
        if the_word[0] == "a" or the_word[0] == "b" or the_word[0] == "c" or the_word[0] == "d" or the_word[0] == "e":
            return self.get_first_letter(the_word, "abcde.txt")
        elif the_word[0] == "f" or the_word[0] == "g" or the_word[0] == "h" or the_word[0] == "i" or the_word[0] == "j":
            return self.get_first_letter(the_word, "fghij.txt")
        elif the_word[0] == "k" or the_word[0] == "l" or the_word[0] == "m" or the_word[0] == "n" or the_word[0] == "o":
            return self.get_first_letter(the_word, "klmno.txt")
        elif the_word[0] == "p" or the_word[0] == "q" or the_word[0] == "r" or the_word[0] == "s" or the_word[0] == "t":
            return self.get_first_letter(the_word, "pqrst.txt")
        elif the_word[0] == "u" or the_word[0] == "v" or the_word[0] == "w" or the_word[0] == "x" or the_word[
            0] == "y" or the_word[0] == "z":
            return self.get_first_letter(the_word, "uvwxyz.txt")

    def get_first_letter(self, the_word, text_file):
        self.verb_text_file = "/home/ricardo/ws/AprilProcesser/AprilProcesser/aprilprocesser/models/books/verbs/verbos_" + text_file
        self.noun_text_file = "/home/ricardo/ws/AprilProcesser/AprilProcesser/aprilprocesser/models/books/nouns/sustantivos_" + text_file
        self.adjective_text_file = "/home/ricardo/ws/AprilProcesser/AprilProcesser/aprilprocesser/models/books/adjectives/adjetivos_" + text_file
        self.pronoun_text_file = "/home/ricardo/ws/AprilProcesser/AprilProcesser/aprilprocesser/models/books/pronouns/pronombres_" + text_file
        return self.finder_brain(the_word, self.verb_text_file, self.noun_text_file, self.adjective_text_file,
                                 self.pronoun_text_file)

    def finder_brain(self, word, verb_text_file, noun_text_file, adjective_text_file, pronoun_text_file):
        finder_of_verb = self.find_words(word, "verb", verb_text_file)
        finder_of_noun = self.find_words(word, "noun", noun_text_file)
        finder_of_adjective = self.find_words(word, "adjective", adjective_text_file)
        finder_of_pronoun = self.find_words(word, "pronoun", pronoun_text_file)
        if finder_of_verb != "It founded" and finder_of_noun != "It founded" and finder_of_adjective != "It founded" and finder_of_pronoun != "It founded":
            self.count_other_words += 1
        return self.count_other_words

    def find_words(self, find_word, type_of_counter, type_text_file):
        with open(type_text_file, 'r') as f:
            for line in f:
                for word in line.split():
                    if find_word == word.lower():
                        if type_of_counter == "verb":
                            self.count_verbs += 1
                            return "It founded"
                        elif type_of_counter == "noun":
                            self.count_nouns += 1
                            return "It founded"
                        elif type_of_counter == "adjective":
                            self.count_adjective += 1
                            return "It founded"
                        elif type_of_counter == "pronoun":
                            self.count_pronouns += 1
                            return "It founded"

    def get_result(self):
        self.vector.append({'verbs': self.count_verbs, 'nouns': self.count_nouns, 'adjectives': self.count_adjective,
                            'pronouns': self.count_pronouns, 'other_words': self.count_other_words,
                            'total_words': self.count_total_words})
        return self.vector
