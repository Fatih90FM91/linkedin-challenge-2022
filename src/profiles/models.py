from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    author =models.ForeignKey(User,on_delete=models.CASCADE)
    job_title = models.CharField(max_length=50 ,default="full stack developer" )


    def __str__(self):
        return self.job_title + ' | ' + str(self.author)


    # def get_absolute_url(self):
    #     return reverse("home")