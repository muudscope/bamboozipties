from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 100, null = False)
    name = models.CharField(max_length = 100, null = False)
    content = models.TextField()

