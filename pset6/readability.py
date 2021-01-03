def main():
    grader = Readability(input("Text: "))
    grade = grader.grade
    if grade == "<1":
        print("Before Grade 1")
    elif grade == "16+":
        print("Grade 16+")
    else:
        print("Grade " + str(grade))


class Readability:
    def __init__(self, text):
        self.word_list = text.split()
        self.stripped_word_list = self.clear_punc()

        self.sentences = self.count_sentences()
        self.words = len(self.stripped_word_list)
        self.letters = self.count_letters()
        self.grade = self.calculate_grade()

    def count_sentences(self):
        word_list = self.word_list
        sentences = 0
        for word in word_list:
            word = list(word)
            last = ord(word[-1])
            s_last = ord(word[-2])
            if last == 46 or last == 63 or last == 33:
                sentences += 1
            elif last == 34 and s_last == 46 or s_last == 63 or s_last == 33 :
                sentences += 1
        return sentences

    def clear_punc(self):
        stripped_word_list = [self.clear_punc_word(word) for word in self.word_list]
        return stripped_word_list

    def clear_punc_word(self, word):
        word = list(word)
        last = ord(word[-1])
        while not((last > 64 and last < 91) or (last > 96 and last < 123)):
            word.pop()
            last = ord(word[-1])
        return word


    def count_letters(self):
        word_list = self.word_list
        letters = 0
        for word in word_list:
            letters += len(word)
        return letters

    def calculate_grade(self):
        letters = self.letters
        sentences = self.sentences
        words = self.words
        L = letters * 100 / words
        S = sentences * 100 / words
        grade = round(0.0588 * L - 0.296 * S - 15.8)
        if grade < 1:
            return "<1"
        elif grade >= 16:
            return "16+"
        else:
            return grade

if __name__ == "__main__":
    main()
