from django.db import models
from django.contrib.auth.models import User

# need db hold users and wishlist 
# two table ( user - wishlist )
  # databaste 
  # based on ORM (object realtional mapping) which make you write db table through python code 
  # class name should start with Capital latter 
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.CharField(max_length=100)
    title = models.CharField(max_length=500) 
    authors = models.CharField(max_length=500, blank=True)
    thumbnail = models.URLField(max_length=500, blank=True) #image
    info_link = models.URLField(max_length=500, blank=True)


    def __str__(self):
        return f"{self.title} - {self.user.username}"
    
# now the class output willl be in string format to read 

  