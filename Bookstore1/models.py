from django.db import models
from django.contrib.auth.models import User

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.CharField(max_length=100)
    title = models.CharField(max_length=500)  # بدل 255
    authors = models.CharField(max_length=500, blank=True)
    thumbnail = models.URLField(max_length=500, blank=True)
    info_link = models.URLField(max_length=500, blank=True)


    def __str__(self):
        return f"{self.title} - {self.user.username}"
    


  