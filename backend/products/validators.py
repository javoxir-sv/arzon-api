from .models import Product          #this is the 2nd version of inline validating in serializers.py

from rest_framework import serializers
from rest_framework.validators import UniqueValidator


def validate_title(value):
    qs = Product.objects.filter(title__iexact=value)
    if qs.exists():
        raise serializers.ValidationError(f"{value} is already a product name.")
    return value


def validate_title_no_hello(value):
    suckers  = ['suck', 'fuck', 'sex', 'mexroj', 'niggggg', 'nigga']
    for word in suckers:
        if word in value.lower():
            raise serializers.ValidationError(f"{word} is not allowed you fucker.")
        return value


unique_product_title = UniqueValidator(queryset=Product.objects.all(), lookup='iexact')
