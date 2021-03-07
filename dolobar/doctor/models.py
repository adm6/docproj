from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='static/doctor', default='my_photo.png')
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title