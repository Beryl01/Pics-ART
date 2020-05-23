from __future__ import unicode_literals
from django.db import models

# Create your models here.
 
class Image(models.Model):
    Name = models.CharField(max_length=60)
    description = models.TextField(default=Deafult_desc)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/' ,default='default.jpg')

    def __str__(self):
        return self.Name  

    @classmethod    
    def save_image(self):
        self.save()

    @classmethod
    def delete_image(self):
        self.delete()    

class Category(models.Model):
    Name = models.CharField(max_length=30)

    def __str__(self):
        return self.Name      

    @classmethod
    def save_category(self):
        self.save()
        
    @classmethod
    def delete_category(self):
        self.delete()      

class Location(models.Model):
    place = models.CharField(max_length=30)

    def __str__(self):
        return self.place       

    @classmethod
    def save_location(self):
        self.save()
    
    @classmethod 
    def delete_location(self):
        self.delete()     
  
    

      

    
