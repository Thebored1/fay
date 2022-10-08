from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm

class TimeInput(forms.TimeInput):
    input_type = 'time'

class DateInput(forms.DateInput):
    input_type = 'date'

class ContactForm(ModelForm):
    class Meta:
        model = contact
        fields = '__all__'

class BookForm(ModelForm):
    class Meta:
        model = book
        fields = '__all__'
        widgets = {
            'time': TimeInput(),
            'date': DateInput(),
        }




class UserCreateForm(UserCreationForm):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=100,null=True)
    phone_no = models.CharField(null=True)

    class Meta:
        model = User
        fields = 'username', 'first_name', 'email', 'last_name', 'password1', 'password2'
        