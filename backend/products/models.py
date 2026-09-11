from django.utils.text import slugify
from django.db import models
from django.conf import settings
from django.db.models import Q
User = settings.AUTH_USER_MODEL
from stores.models import Store


class ProductQuerySet(models.QuerySet):
    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(description__icontains=query) # this is where we search for the query
        qs = self.filter(lookup)
        if user is not None:
            qs2 = self.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs

class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)



class Product(models.Model):
    store = models.ForeignKey(Store, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    sale_price = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    is_discount = models.BooleanField(null=False, blank=False, default=False)
    created_at = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(null=False, blank=False, default=True)
    image_url = models.URLField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    objects = ProductManager()

    def __str__(self):
        return f"ID:{self.pk} | ST:{self.store} - {self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/products/{self.slug}/"

    @property
    def url(self):
        return self.get_absolute_url()

    @property
    def path(self):
        return f"/products/{self.slug}"

    @property
    def body(self):
        return self.description

