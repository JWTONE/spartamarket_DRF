from django.db import models

class Products(models.Model): 
    title = models.CharField(max_length=30, default='')
    content = models.TextField(blank=True)
    images = models.ImageField(upload_to='./products/')
    price = models.IntegerField()
    
    def __str__(self):
        return self.title