from rest_framework import serializers
from rest_framework.reverse import reverse

from .validators import validate_title_no_hello, unique_product_title
from .models import Product

from api.serializers import UserPublicSerializer


class ProductSerializer(serializers.ModelSerializer):
    # owner = UserPublicSerializer(source='user', read_only=True)

#    related_products = ProductInlineSerializer(source='user.product_set.all', read_only=True, many=True)
#    my_discount = serializers.SerializerMethodField(read_only=True)

    tags = serializers.ListField(child=serializers.CharField(max_length=50), required=False)
    # edit_url = serializers.SerializerMethodField(read_only=True)

    url = serializers.HyperlinkedIdentityField( #that's the easiest way to do it, believe me
        view_name='product-detail',
        lookup_field = 'slug',
    )
    title = serializers.CharField(validators=[validate_title_no_hello, unique_product_title])
#    name = serializers.CharField(source='title', read_only=True)
#    email = serializers.EmailField(write_only=True)

    # body = serializers.CharField(source='content')   #links the body up with content so we can update it too
    class Meta:
        model = Product
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

            # some mo're
            'pk',
            'url',
            'url_origin',
            # 'edit_url',
            'path',
        ]


    # def get_my_discount(self, obj):
    #     return obj.get_discount()

    def validate_title(self, value):
        request = self.context.get('request')
        store = request.store
        qs = Product.objects.filter(store=store, title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} is already a product name.")
        return value

    # def get_edit_url(self, obj):
    #     request = self.context.get('request')
    #
    #     if request is None:
    #         return None
    #     return reverse("product-edit", kwargs={"slug":obj.slug}, request=request)




#    def create(self, validated_data):
#        #email = validated_data.pop('email')
#        #return Product.objects.create(**validated_data)
#        obj = super().create(validated_data)
#        #print(email, obj)
#        return obj
#
#    def update(self, instance, validated_data):
#        email = validated_data.pop('email')
#        #instance.title = validated_data.get('title')
#        return super().update(instance, validated_data)    #instance




