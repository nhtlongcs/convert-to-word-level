import os

from .algorithms import split_phrase_to_words


class Splitter:
    def __init__(self, language='vi'):
        self.language = language
        self.update_dict(f'dicts/{language}.txt')

    def update_dict(self, dict_path):
        module_path = os.path.dirname(__file__)

        dict_path = os.path.join(module_path, dict_path)
        word_dict = {}
        f = open(dict_path, 'r')
        lines = f.readlines()
        for l in lines:
            l = l.strip().upper()
            word_dict[l] = True
        self.dict = word_dict
        return self.dict

    def split(self, phrase):
        return split_phrase_to_words(phrase, self.dict)
