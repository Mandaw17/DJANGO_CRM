from django import forms 
from django.contrib.auth.models import User
from apps.userprofile.models import Profile
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optionnal')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optionnal')
    email = forms.EmailField(max_length=254, required=False, help_text='Enter a valid email adress')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ] 


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name', 
            'last_name', 
            'email',
        ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'bio', 
            'phone_number', 
            'birth_date', 
            'profile_image',
        ] 
 