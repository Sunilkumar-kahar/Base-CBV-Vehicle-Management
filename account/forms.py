from django import forms
from .models import CustomUser

class Registration(forms.ModelForm):
    role = forms.ChoiceField(choices = [("", 'Select Role')] + CustomUser.options, required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = CustomUser
        fields = ['user_name', 'role', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super().clean()
        user_name = cleaned_data.get('user_name')
        pswrd = cleaned_data.get('password')
        cnfrm_pswrd = cleaned_data.get('confirm_password')

        if CustomUser.objects.filter(user_name = user_name).exists():
            self.add_error('user_name', 'This user name already exist.')

        if pswrd != cnfrm_pswrd:
            self.add_error('confirm_password', 'Password and Confirm Password do not match.')
        return cleaned_data


class Login(forms.Form):
    user_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

