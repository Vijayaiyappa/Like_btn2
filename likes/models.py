from django.db import models
from django.db.models import Model
# Create your models here.


class liked_data(Model):
    def __str__(self):
        return self.__class__.__name__
    post_id = models.IntegerField()
    user_id = models.IntegerField()
