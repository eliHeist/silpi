from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='homepage'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('terms-privacy/', views.TermsAndPrivacyView.as_view(), name='terms-privacy'),
    path('services/micro-loans/', views.MicroLoanView.as_view(), name='micro-loans'),
    path('services/paint/', views.PaintView.as_view(), name='paint'),
]