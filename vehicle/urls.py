from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('form/', VehicleForm.as_view(), name = 'vehicle_form'),
    path('detail/', VehicleList.as_view(), name = 'vehicle_detail'),
    path('change/<int:id>/', UpdateVehicle.as_view(), name = 'edit_vehicle'),
    path('delete/<int:id>/', DeleteVehicle.as_view(), name = 'delete_vehicle'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
]