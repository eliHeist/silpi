from django.urls import path

from cart.views import AddToCartView, CartView, CheckoutAPIView, SuccessView

app_name = 'cart'

urlpatterns = [
    path('checkout/', CartView.as_view(), name='checkout'),
    # ... other URL patterns ...
    path('api/add-to-cart/', AddToCartView.as_view(), name='add-to-cart'),
    path('api/checkout/', CheckoutAPIView.as_view(), name='api-checkout'),
    path('success/', SuccessView.as_view(), name='success'),
]
