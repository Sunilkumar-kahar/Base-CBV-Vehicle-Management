from django.shortcuts import render, redirect
from .forms import Vehicle_form
from .models import Vehicle
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import View


class VehicleForm(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'vehicle.add_vehicle'
    def get(self, request):
        form = Vehicle_form()
        return render(request, 'vehicle/vehicle_form.html', {'form':form})
    
    def post(self, request):
        form = Vehicle_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicle_form')
        return render(request, 'vehicle/vehicle_form.html', {'form':form})
    

class VehicleList(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'vehicle.view_vehicle'
    def get(self, request):
        vehicles = Vehicle.objects.all()
        return render(request, 'vehicle/vehicle_details.html', {'vehicles':vehicles})


class UpdateVehicle(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'vehicle.change_vehicle'
    def get(self, request, id):
        obj = Vehicle.objects.get(id = id)
        form  = Vehicle_form(instance = obj)
        return render(request, 'vehicle/vehicle_form.html', {'form' : form})
    
    def post(self, request, id):
        obj = Vehicle.objects.get(id = id)
        form = Vehicle_form(request.POST, instance = obj)
        if form.is_valid():
            form.save()
            return redirect('vehicle_detail')
        return render(request, 'vehicle/vehicle_form.html', {'form' : form})

    
class DeleteVehicle(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'vehicle.delete_vehicle'
    def post(self, request, id):
        user = Vehicle.objects.get(id = id)
        user.delete()
        return redirect('vehicle_detail')

