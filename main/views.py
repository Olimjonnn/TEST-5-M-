from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework import viewsets
from rest_framework import filters
from main.models import *
from main.serializer import *


class LogoView(viewsets.ModelViewSet):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    http_method_names = ['get']

    def list(self, request):
        logo = Logo.objects.last()
        log = LogoSerializer(logo)
        return Response(log.data)


class SliderView(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    http_method_names = ['get']


class BlogView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    http_method_names = ['get']


class NewsView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]

    http_method_names = ['get']

    def list(self, request):
        news = News.objects.last()
        new = NewsSerializer(news)
        return Response(new.data)

@api_view(['GET'])
def NewsVW(request):
    new = News.objects.last()
    nw = NewsSerializer(new)
    return Response(nw.data)


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'price']

    http_method_names = ['get']

    @action(['GET'], detail=False)
    def cat(self, request):
        category = request.GET.get('category')
        aa = Product.objects.filter(category_id=category)
        a = ProductSerializer(aa, many=True)
        return Response(a.data)

    @action(['GET'], detail=False)
    def sale(self, request):
        sal = Product.objects.filter(tick=True)
        sa = ProductSerializer(sal, many=True)
        return Response(sa.data)
        
@api_view(['PATCH'])
def ProductPatch(request):
    img1 = request.POST.get("img1")
    category = request.POST.get('category')
    name = request.POST.get('name')
    design = request.POST.get('design')
    stars = request.POST.get('stars')
    price = request.POST.get('price')
    description = request.POST.get('description')
    a = Product.objects.create(img1=img1, category=category, name=name, design=design, stars=stars, price=price, description=description)
    b = ProductSerializer(a)
    return Response(b.data)
    




@api_view(['GET'])
def ProductGet(request):
    product = Product.objects.last()
    pr = ProductSerializer(product)
    return Response(pr.data)

class InfoView(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    http_method_names = ['get']

    def list(self, request):
        info = Info.objects.last()
        inf = InfoSerializer(info)
        return Response(inf.data)

class CartView(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    http_method_names = ['post']
    def create(self, request):
        try:
            product = request.POST.get("product")
            user = request.POST.get("user")
            Cart.objects.create(product_id=product, user_id=user)
            return Response({"Created"})
        except Exception as ar:
            data = {
                'error': f"{ar}"
            }
            return Response(data)

@api_view(['PUT'])
def CartPUT(request, pk):
    product = request.POST.get("product")
    user = request.POST.get("user")
    car = Cart.objects.create(product_id=product, user_id=user)
    ca = CartSerializer(car)
    return Response(ca.data)

@api_view(['PATCH'])
def CartPATCH(request, pk):
    product = request.POST.get("product")
    user = request.POST.get("user")
    car = Cart.objects.create(product_id=product,  user_id=user)
    ca = CartSerializer(car)
    return Response(ca.data)

@api_view(['DELETE'])
def CartDELETE(request, pk):
    product = request.POST.get("product")
    user = request.POST.get("user")
    car = Cart.objects.delete(product_id=product, user_id=user)
    ca = CartSerializer(car)
    return Response(ca.data)

class WishlistView(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    http_method_names = ['post']

    def create(self, request):
        product = request.POST.get("product")
        Wishlist.objects.create(product_id=product)
        return Response({"Created"})

@api_view(['DELETE'])
def WishlistDELETE(request):
    product = request.POST.get("product")
    car = Wishlist.objects.delete(product_id=product)
    ca = WishlistSerializer(car)
    return Response(ca.data)