from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model): #JO -< WO

    title = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Director(models.Model): #WO

    name= models.CharField(max_length=150)
    age = models.CharField(max_length=250)
    img = models.CharField(max_length=5000)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="directors")

    def __str__(self):
            return self.name
