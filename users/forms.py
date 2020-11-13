from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from .models import Customer,User


class CustomerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'username', 'password1', 'password2')

    def save(self, marital_status):
        print("reached")
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        Customer.objects.create(user=user, marital_status = marital_status)
        return user


class CustomerForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone')

