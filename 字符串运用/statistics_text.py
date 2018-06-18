# -*- coding:utf-8 -*-
seq = "The, importationc, of the article editor page text the text can be statistics numbers the number of spaces "

str_result = {}

def deal_word(word):
    return word.lower().strip(",.!)-*_?:;'-\"")

def word_count(content):
    words = content.split()
    str_list = []
    for word in words:
        str_list.append(deal_word(word))

    global str_result
    for word in str_list:
        if word not in str_result:
            str_result[word] = 1
        else:
            str_result[word] += 1
    return str_result

def file_count(path):
    with open(path,'r',encoding='utf-8') as f :
        for line in f :
           word_count(line)
    print(str_result)

class Sequence(object):
    def __init__(self, content):
        self.content = content
        self.str_result = {}

    def deal_word(self):

        return self.content.lower().strip(",.!)-*_?:;'-\"")

    def text_count(self,line):
        self.content = line
        str_list = self.deal_word()
        words = self.content.split()
        str_list = []
        for word in words:
            str_list.append(deal_word(word))


        for word in str_list:
            if word not in self.str_result:
                self.str_result[word] = 1
            else:
                self.str_result[word] += 1
        return self.str_result

    def file_count(self,path):
        with open(path,'r',encoding='utf-8') as f :
            for line in f:
               self.text_count(line)
        print(self.str_result)
        #print(out_dict)

from toolz import frequencies, compose, partial,concatv

if __name__ == "__main__":
    def read_file(path) :
        with open(path, 'r', encoding='utf-8') as f:
            return f

    count_text = compose(frequencies, partial(map, deal_word), str.split,next,read_file)
    #print(count_text("word.txt"))
    # seq1 = Sequence(seq)
    #file_count("word.txt")
