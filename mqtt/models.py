from mongoengine import Document, StringField, IntField



class RackInventory(Document):
    rack_number = StringField(required=True, unique=True)
    level_0 = IntField(default=0)
    level_1 = IntField(default=0)
    level_2 = IntField(default=0)
    level_3 = IntField(default=0)

    meta = {
        'collection': 'Inventory_level'
    }
