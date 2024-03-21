from mongoengine import Document, EmbeddedDocument, StringField, BooleanField, IntField, ListField, EmbeddedDocumentField

class QualityControl(EmbeddedDocument):
    passed = BooleanField(default=True)
    testing_results = StringField()
    certifications = ListField(StringField())

class Package(EmbeddedDocument):
    package_number = StringField(required=True)
    rfid = StringField(required=True)
    product_type = StringField()
    part_number = StringField()
    manufacturer = StringField()
    manufacturing_date = StringField()
    batch_code = StringField()
    quality_control = EmbeddedDocumentField(QualityControl)
    handling_instructions = StringField()

class EmptySpaces(EmbeddedDocument):
    full = IntField(default=10)
    sub_storage = IntField(default=0)

class Level(EmbeddedDocument):
    level_number = StringField(required=True)
    packages = ListField(EmbeddedDocumentField(Package))
    empty_spaces = EmbeddedDocumentField(EmptySpaces)

class Inventory(Document):
    rack_number = StringField(required=True, unique=True)
    levels = ListField(EmbeddedDocumentField(Level))
    
    meta = {
        'collection': 'Inventory_level'  # Specify the collection name
    }