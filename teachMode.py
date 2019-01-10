# -*- coding: UTF-8 -*-

import db as db

def learn_new_word(word):
    word_list = word.split(' ')
    req = word_list[1]
    res = word_list[2]
    db.insert_learning(req, res)
    return '學會「{0}」囉~'.format(req)

def responding(word):
    return db.get_learning(word)