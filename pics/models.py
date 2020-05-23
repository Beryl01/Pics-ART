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

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(value)    

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

    @classmethod
    def update_category(cls, id, new_category):
        cls.objects.filter(id=id).update(Category=new_category)    
     

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
  
    @classmethod
    def update_location(cls, id, new_location):
        cls.objects.filter(id=id).update(location=new_location)  
    

      

    
