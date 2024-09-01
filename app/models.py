from mongoengine import Document, StringField, FloatField, ReferenceField

class User(Document):
    username = StringField(required=True, unique=True)
    email = StringField(required=True, unique=True)
    hashed_password = StringField(required=True)

    def __str__(self):
        return f"User(username={self.username}, email={self.email})"

class Item(Document):
    name = StringField(required=True)
    price = FloatField(required=True)
    owner = ReferenceField(User, required=True)

    def __str__(self):
        return f"Item(name={self.name}, price={self.price}, owner={self.owner})"
