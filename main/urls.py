from django.urls import path

from main.views import AboutView, IndexView, TermsAndPrivacyView

app_name = 'main'

urlpatterns = [
    path('', IndexView.as_view(), name='homepage'),
    path('about/', AboutView.as_view(), name='about'),
    path('terms-privacy/', TermsAndPrivacyView.as_view(), name='terms-privacy'),
]