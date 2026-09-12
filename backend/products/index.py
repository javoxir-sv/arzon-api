from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Product

@register(Product)
class ProductIndex(AlgoliaIndex):
    fields = [
            'store',
            'title',
            'description',
            'price',
            'sale_price',
            'on_sale',
            'sale_begin',
            'sale_end',
            'is_available',
            'image_url',
            'slug',
            'created_at',
            'tags',
    ]

    settings = {
        'searchableAttributes':['title', 'description'],
        'attributesForFaceting': ['store','is_available'],
    }
    # index_name = 'arzon_products'

