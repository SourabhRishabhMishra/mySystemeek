# import the standard Django Model 
# from built-in library 
from django.db import models 

# declare a new model with a name "GeeksModel" 
class Album(models.Model): 
    title = models.CharField(max_length = 30) 
    artist = models.CharField(max_length = 30) 
    genre = models.CharField(max_length = 30) 
  
    def __str__(self): 
        return self.title 
  
class Song(models.Model): 
    name = models.CharField(max_length = 100) 
    album = models.ForeignKey(Album, on_delete = models.CASCADE) 
  
    def __str__(self): 
        return self.name
