from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from accounts.admin import user_admin

urlpatterns = [
    path('super-admin/', admin.site.urls),
    path('admin/', user_admin.urls),
    path('products/', include('products.urls', namespace='products')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('consultancy/', include('consultancy.urls', namespace='consultancy')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('vehicles/', include('vehicles.urls', namespace='vehicles')),
    path('posts/', include('posts.urls', namespace='posts')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('', include('main.urls', namespace='main')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
