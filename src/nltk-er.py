from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.chunk import conlltags2tree, tree2conlltags
import texts_db as texts
 
text = texts.bengala

ne_tree = ne_chunk(pos_tag(word_tokenize(text)))
 
iob_tagged = tree2conlltags(ne_tree)

def wordextractor(text):

    #bring the tuple back to lists to work with it
    words, tags, pos = zip(*text)
    words = list(words)
    pos = list(pos)
    c = list()
    i=0
    while i<= len(text)-1:
        #get words with have pos B-PERSON or I-PERSON
        if pos[i] == 'B-PERSON':
            c = c+[words[i]]
        elif pos[i] == 'I-PERSON':
            c = c+[words[i]]
        i=i+1

    return c
 
print(wordextractor(tree2conlltags(ne_chunk(pos_tag(word_tokenize(text))))))