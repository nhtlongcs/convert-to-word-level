import os

from .algorithms import split_phrase_to_words

s1 = u'ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'
s0 = u'AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOoUuAaAaAaAaAaAaAaAaAaAaAaAaEeEeEeEeEeEeEeEeIiIiOoOoOoOoOoOoOoOoOoOoOoOoUuUuUuUuUuUuUuYyYyYyYy'


def remove_accents(input_str):
    s = ''
    for c in input_str:
        if c in s1:
            s += s0[s1.index(c)]
        else:
            s += c
    return s


class Splitter:

    def __init__(self, languages=['vi']):
        self.languages = languages
        self.dict = {}
        for lang in languages:
            if lang == 'vi' or lang == "teencode":
                self.update_dict(f'dicts/{lang}.txt', rm_accents=True)
            self.update_dict(f'dicts/{lang}.txt')

    def update_dict(self, dict_path, rm_accents=False):
        module_path = os.path.dirname(__file__)
        dict_path = os.path.join(module_path, dict_path)
        word_dict = {}
        f = open(dict_path, 'r')
        lines = f.readlines()
        for l in lines:
            l = l.strip().upper()
            word_dict[l] = True
            if rm_accents:
                word_dict[remove_accents(l)] = True
        self.dict.update(word_dict)

    def split(self, phrase):
        return split_phrase_to_words(phrase, self.dict)
