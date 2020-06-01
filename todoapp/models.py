from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User
from django.db.models import DateTimeField





# Create your models here.

class Task(TimeStampedModel):
    STATUSES = (
        (0, 'Not Completed'),
        (1, 'Completed'),
    )
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateTimeField()
    status = models.PositiveSmallIntegerField(choices=STATUSES, default=0)
    
    
    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)