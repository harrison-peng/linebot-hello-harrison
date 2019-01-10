import db as db

def learn_new_word(word):
    word_list = word.split(' ')
    req = word_list[1]
    res = word_list[2]
    db.insert(req, res)
    return '學會了'

def responding(word):
    return db.get(word)
