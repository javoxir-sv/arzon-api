from rest_framework import serializers



class UserPublicInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField( #that's the easiest way to do it, believe me
        view_name='product-detail',
        lookup_field = 'slug',
        read_only=True,
    )
    title = serializers.CharField(read_only=True)


class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
#    other_products = serializers.SerializerMethodField(read_only=True)
#
#    def get_other_products(self, obj):
##        request = self.context.get('request')
#        user = obj
#        my_products_qs = user.product_set.all()[:5]
#        return UserPublicInlineSerializer(my_products_qs, many=True, context=self.context).data
