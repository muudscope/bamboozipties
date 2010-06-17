from django.db import models
from bzt.bzt_utils import SerializableModel

class Post(SerializableModel):
    title = models.CharField(max_length = 100, null = False)
    name = models.CharField(max_length = 100, null = False)
    content = models.TextField()

