# -*- coding: UTF-8 -*-

import pymongo
import random

def connect(col_name):
    myclient = pymongo.MongoClient("mongodb://harrison:linebot2019@ds253324.mlab.com:53324/linebot-hello-harrison")
    db = myclient['linebot-hello-harrison']
    collection = db[col_name]
    return collection

def insert_learning(req, res):
    collection = connect('learning')

    doc = collection.find_one({'request': req})
    if doc is None:
        data = {
            'request': req,
            'response': res
            }

        result = collection.insert_one(data)
    else:
        id = doc['_id']
        query = {'_id': id}
        new_value = { '$set': { 'response': res } }
        result = collection.update_one(query, new_value)
    return result

def get_learning(req):
    collection = connect('learning')
    res = collection.find_one({'request': req})
    if res is None:
        return None
    else:
        return res['response']

def insert_game(user_id):
    collection = connect('game')

    answer = ''
    answer_list = random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 4)
    for item in answer_list:
        answer += item

    doc = collection.find_one({'user_id': user_id})
    if doc is None:
        data = {
            'user_id': user_id,
            'answer': answer,
            'play': True,
            'count': 0
        }
        collection.insert_one(data)
    else:
        id = doc['_id']
        query = {'_id': id}
        new_value = { 
            '$set': { 
                'answer': answer,
                'play': True ,
                'count': 0
                } 
        }
        collection.update_one(query, new_value)

def user_play_game(user_id):
    collection = connect('game')

    user_data = collection.find_one({'user_id': user_id})
    if user_data is None:
        return False
    else:
        return user_data['play']

def get_game_answer(user_id):
    collection = connect('game')

    user_data = collection.find_one({'user_id': user_id})
    
    query = {'_id': user_id}
    new_value = {
        '$inc': {
            'count': 1
        }
    }
    collection.update_one(query, new_value)
    return user_data['answer']

def get_game_count(user_id):
    collection = connect('game')
    return collection.find_one({'user_id': user_id})['count']

def set_game_play_false(user_id):
    collection = connect('game')

    query = {'_id': user_id}
    new_value = {
        '$set': {
            'play': False,
            'answer': ''
        }
    }
    collection.update_one(query, new_value)