import pymongo

def connect():
    myclient = pymongo.MongoClient("mongodb://harrison:linebot2019@ds253324.mlab.com:53324/linebot-hello-harrison")
    db = myclient['linebot-hello-harrison']
    collection = db['learning']
    return collection

def insert(req, res):
    collection = connect()

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
        new_value = { "$set": { "response": res } }
        result = collection.update_one(query, new_value)
    return result

def get(req):
    collection = connect()
    return collection.find_one({'request': req})['response']
