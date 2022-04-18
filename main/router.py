from rest_framework import routers
from main.views import *

router = routers.DefaultRouter()

router.register("logo",LogoView)
router.register("slider",SliderView)
router.register("blog",BlogView)
router.register("news",NewsView)
router.register("product",ProductView)
router.register("info",InfoView)
router.register("cart",CartView)
router.register("wishlist",WishlistView)
