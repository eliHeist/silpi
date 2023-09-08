from products.views import CategoryListView, ProductCreateView, ProductDeleteView, ProductDetailView, ProductListView, ProductUpdateView
from django.urls import path


app_name = 'products'

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('categories/<int:pk>/', ProductListView.as_view(), name='products-by-category'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    
    path('', ProductListView.as_view(), name='all-products'),
    path('create/', ProductCreateView.as_view(), name='product-create'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
]
