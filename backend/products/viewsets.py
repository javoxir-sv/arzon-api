from rest_framework import viewsets, mixins

from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    '''
    get
    post
    put 
    delete
    patch
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'




class ProductGenericViewSet(          # SO IT ONLY PROVIDES 2 ENDPOINT OR WHATEVER TYPE SHI, WE CAN'T DO MORE THAN WHAT WE PROVIDE HERE
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
    ):
    '''
    get
    get -> retrieve
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'