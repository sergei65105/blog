from django.db import models

# Create your models here.
class Video(models.Model):
    name = models.CharField(max_length=50)
    embed_code = models.CharField(max_length=100)
    is_published = models.BooleanField(default=True)