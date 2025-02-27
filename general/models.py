from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=155)
    about = models.CharField(max_length=1000)
    details = models.TextField()
    fees = models.IntegerField()
    icon = models.ImageField(upload_to='icons/',default='../static/graphics/techfest.svg')

    def __str__(self):
        return self.name