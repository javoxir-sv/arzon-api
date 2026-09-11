from django.db import models

# Create your models here.

from django.conf import settings
from django.db.models import Q, CharField

User = settings.AUTH_USER_MODEL



class Store(models.Model):
    name = CharField(max_length=100, null=False, blank=False, default="Gogo Gaga")

