from django.urls import path

from vehicles.views import VehicleListView, VehicleRequestView

app_name = 'vehicles'

urlpatterns = [
    path('', VehicleListView.as_view(), name='list'),
    path('<int:pk>/request/', VehicleRequestView.as_view(), name='request'),
]