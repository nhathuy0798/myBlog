from django.db import models
from numpy import tile
from django.conf import settings

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null = True)
    price = models.IntegerField()
    def __str__(self):
        return self.title

class Comment_item(models.Model):
    post = models.ForeignKey(Product, on_delete=models.CASCADE, related_name= "comments")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)