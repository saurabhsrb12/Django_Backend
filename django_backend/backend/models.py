from django.contrib.auth.models import User
from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Work(models.Model):
    YOUTUBE = 'YT'
    INSTAGRAM = 'IG'
    OTHER = 'OT'
    WORK_TYPE_CHOICES = (
        (YOUTUBE, 'Youtube'),
        (INSTAGRAM, 'Instagram'),
        (OTHER, 'Other'),
    )

    link = models.URLField()
    work_type = models.CharField(max_length=2, choices=WORK_TYPE_CHOICES)
    artists = models.ManyToManyField('Artist')

    def __str__(self):
        return self.link

class Artist(models.Model):
    name = models.CharField(max_length=255)
    works = models.ManyToManyField(Work)

    def __str__(self):
        return self.name
