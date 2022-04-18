from rest_framework import serializers
from main.models import *

class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = "__all__"

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = "__all__"

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = "__all__"

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"
