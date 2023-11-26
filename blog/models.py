from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    img = models.ImageField(upload_to='images')
    likes = models.IntegerField(default=0)