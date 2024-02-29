from mongoengine import Document, StringField, IntField

class Person(Document):
    nom = StringField()
    prenom = StringField()
    age = IntField()
    cp = IntField()

    meta = {'collection': 'personnes'}  # Specify the collection name
