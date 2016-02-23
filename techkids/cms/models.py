from mongoengine import *

# Create your models here.
class Node(Document):
    title = StringField(max_length = 100)