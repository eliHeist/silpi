from django.urls import path

from consultancy.views import ConsultancyListView, IndexView

app_name = 'consultancy'

urlpatterns = [
    path('', IndexView.as_view(), name='consultancy'),
    path('portfolio/', ConsultancyListView.as_view(), name='portfolio'),
]