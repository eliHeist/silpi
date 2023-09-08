from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls', namespace='products')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('consultancy/', include('consultancy.urls', namespace='consultancy')),
    path('services/', include('services.urls', namespace='services')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('', include('main.urls', namespace='main')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
