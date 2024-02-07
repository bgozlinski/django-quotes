from mongoengine import Document, StringField


class Quote(Document):
    quote = StringField(required=True)
    author = StringField(required=True)

    meta = {'collection': 'quotes'}
    