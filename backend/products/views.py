from rest_framework import generics, mixins        #, permissions, authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import Http404

#from api.authentication import TokenAuthentication   I managed it with mixins
from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin

from .models import Product
#from api.permissions import IsStaffEditorPermission   I managed it with mixins
from .serializers import ProductSerializer



class ProductDetailAPIView(UserQuerySetMixin, StaffEditorPermissionMixin, generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    #authentication_classes = [authentication.SessionAuthentication]   ##that's how we keep going/adding persmissions, we are not editing permissions
    #permission_classes = [permissions.DjangoModelPermissions]    ## we are just putting restrictions to users who already has defined permissions


class ProductListCreateAPIView(UserQuerySetMixin, StaffEditorPermissionMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    '''authentication_classes = [           WE DON'T NEED THEM SINCE WE SET IT UP IN SETTINGS.PY
        TokenAuthentication,
        authentication.SessionAuthentication
        ]'''
    #permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]  #permissions.DjangoModelPermissions

    def perform_create(self, serializer):
#        email = serializer.validated_data.pop('email')
        #serializer.save(user=self.request.user) I could do that if I had One To Many relationship with it
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title

        serializer.save(user=self.request.user, content=content)

#    def get_queryset(self):
#        qs = super().get_queryset()
#        request = self.request
#        return qs.filter(user=request.user)
    




class ProductUpdateAPIView(UserQuerySetMixin, StaffEditorPermissionMixin, generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
#    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class ProductDeleteAPIView(UserQuerySetMixin, StaffEditorPermissionMixin, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'  # it's already default we don't even need this
#    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

#Just repeating the deault stuff:
    def perform_destroy(self, instance):
        super().perform_destroy(instance)




class ProductMixinView(
                        UserQuerySetMixin, 
                        StaffEditorPermissionMixin,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.ListModelMixin, 
                        generics.GenericAPIView
                        ):                            # We can out the mixing straight up before it, that's why it's called mixin
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
#    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def get(self, request, *args, **kwargs):
        # print(args, kwargs)
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = "Ohhhhhhh yeeeeeeeeeeeeeeeeaaaaaaaaaaaaaaaaaaaaaaaaa"
        serializer.save(content=content)

### Duuuuuude I have to learn everything about these mixins, cuz they are amazing!!!!!!!!!!!!!!!
# --- f*** off bro I don't have a time.


@api_view(["GET", "POST"])
def product_alt_view(request, pk=None):

    method = request.method

    if method == 'GET':
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data

            return Response(data)

        #list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)


    if method == "POST":
        #create an item
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title

            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid" : "not good data here"}, status=400)
