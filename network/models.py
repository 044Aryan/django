from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)

class Dweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dweets')
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)