from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL



class Store(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=400, null=True, blank=True)
    homepage = models.URLField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    tags = ArrayField(models.CharField(max_length=50), default=list, blank=True)


    def __str__(self):
        return self.name


