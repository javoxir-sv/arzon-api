from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Product

@register(Product)
class ProductIndex(AlgoliaIndex):
    fields = [
        'title',
        'description',
        'price',
        'sale_price',
        'created_at',
        'image_url',
        'store',
        'is_available',
        'is_discount',
        'path',
        'url',
        'slug',
    ]

    settings = {
        'searchableAttributes':['title', 'description'],
        'attributesForFaceting': ['store',],
    }

