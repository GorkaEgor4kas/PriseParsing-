from django.db import models

# Create your models here.
#this is a class for 'success' page, with a list of all typed products
class listProduct(models.Model):
    #here i need cells for product's URL and it's name
    product_link = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"name: {self.name} -- link: {self.product_link}"