# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list = []):
        self.list = list
        new_list = []
        for item in list:
            if sorted(self.word) == sorted(item):
                new_list.append(item)
            else:
                return new_list