from django.db import models
from accounts.models import User

class Products(models.Model): 
    title = models.CharField(max_length=30, default='')
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    images = models.ImageField(upload_to='./products/')
    price = models.IntegerField()
    
    def __str__(self):
        return self.title