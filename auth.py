import demo
db=demo.client['meeting']
collection=db['room']
dictionary={
    'name':'fazil',
    'marks':56
}
collection.insert_one(document=dictionary)