from django.db import models

# Create your models here.


class Confession(models.Model):
    content = models.TextField(max_length=100, blank=False, null=False)

    date = models.DateTimeField(auto_now_add=True)

    likes = models.PositiveIntegerField(default=0)

    moderated = models.BooleanField(default=False)

    def __str__(self):
         # returns the first 50 characters of a confession
        return f'{self.content[0:51]} ---- {self.date}'

class Comments(models.Model):
    reply = models.CharField(max_length=150, blank=False, null=False)

    likes = models.PositiveIntegerField(default=0)


