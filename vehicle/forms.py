from django import forms
from .models import Vehicle

class Vehicle_form(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.fields['vehicle_type'].choices = [('', 'Select Wheelar'),] + list(self.fields['vehicle_type'].choices)