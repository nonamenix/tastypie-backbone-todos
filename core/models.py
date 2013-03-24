from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return self.title