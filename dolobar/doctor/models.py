from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='static/doctor', default='my_photo.png')
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title


class Marathon(models.Model):
    title = models.CharField(max_length=100)
    information = models.TextField(null=True)
    image = models.ImageField(upload_to='static/doctor', default='def_img_for_articles.jpg')
    starting_day = models.DateField()
    ending_day = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)
    results = models.TextField(default="Not finished!")

    def __str__(self):
        return self.title

    @property
    def until_end(self):
        return (self.ending_day - datetime.date.today()).days

    @property
    def until_start(self):
        return (self.starting_day - datetime.date.today()).days


class Reception(models.Model):  # Klinikada qabul
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='static/doctor', default='def_img_for_articles.jpg')
    # created_at = models.DateTimeField()

    def __str__(self):
        return self.title


class Consultation(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='static/doctor', default='def_img_for_articles.jpg')
    # created_at = models.DateTimeField()

    def __str__(self):
        return self.title
