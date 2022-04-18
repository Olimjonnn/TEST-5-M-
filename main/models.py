from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    type = models.IntegerField(choices=(
        (1, 'admin'),
        (2, 'client'),
    ), default=2)
    phone = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.username
    
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Logo(models.Model):
    img = models.ImageField(upload_to='img/')

class Slider(models.Model):
    img = models.ImageField(upload_to='Slider/')
    title1 = models.CharField(max_length=50)
    title2 = models.CharField(max_length=50)
    text = models.CharField(max_length=150)

class Blog(models.Model):
    img = models.ImageField(upload_to="Blog/")
    title = models.CharField(max_length=200)
    text = models.TextField()

class News(models.Model):
    img = models.ImageField(upload_to="News/")
    sale = models.IntegerField()
    name = models.CharField(max_length=30)
    text = models.CharField(max_length=50)

class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    img1 = models.ImageField(upload_to="Product/")
    img2 = models.ImageField(upload_to="Product/", blank=True, null=True)
    img3 = models.ImageField(upload_to="Product/", blank=True, null=True)
    img4 = models.ImageField(upload_to="Product/", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    design = models.CharField(max_length=200, blank=True, null=True)
    stars = models.IntegerField()
    price = models.IntegerField()
    base_price = models.IntegerField(blank=True, null=True)
    description = models.TextField()
    sale = models.IntegerField(blank=True, null=True)
    tick = models.BooleanField(default=False)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Info(models.Model):
    phone = models.IntegerField()
    email = models.EmailField()
    facebook = models.CharField(max_length=500)
    telegram = models.CharField(max_length=500)
    instagram = models.CharField(max_length=500)
    twitter = models.CharField(max_length=500)
