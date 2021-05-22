from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# just here to some changes
# another change
# this is the change in new-branch-1


class Chat(models.Model):
    test = models.CharField(max_length=100)
    chat = models.CharField(max_length=50)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
