
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main.router import router
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/newss/get', NewsVW),
    path('api/product/get', ProductGet),
    path('api/cart/put/<int:pk>', CartPUT),
    path('api/cart/patch/<int:pk>', CartPATCH),
    path('api/cart/delete/<int:pk>', CartDELETE),
    path('api/product/patch/<int:pk>', ProductPatch),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
