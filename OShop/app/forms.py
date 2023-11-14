from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation
from .models import OrderPlaced


class CoustomerRegistrationFrom(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email':'Email'}
        widgets = {'username': forms.TextInput(attrs={'class':'form-control'})}


class UserLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("Password"),strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))

class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password',strip=False, widget=forms.PasswordInput(attrs={'class':'form-control', 'autocomplete':'current-password', 'autofocus':True}))
    new_password1 = forms.CharField(label='New Password',strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label='Confirm New Password',strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control'}))


class UserPasswordResetForms(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class':'form-control'}))

class UserSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password',strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label='Confirm New Password',strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control'}))

class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = OrderPlaced
        fields = ['name', 'state', 'location', 'phone_number', 'payment_method']
        labels = {'payment_method':'Select Payment Method'}

        widgets = {
            'state':forms.Select(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'location':forms.TextInput(attrs={'class':'form-control'}),
            'phone_number':forms.NumberInput(attrs={'class':'form-control'}),
            'payment_method':forms.Select(attrs={'class':'form-control'}),
            
        }