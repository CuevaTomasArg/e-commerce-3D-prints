from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import  User
from .models import *

class CategoryForm(forms.Form):
    name = forms.CharField(max_length=75)
    brand = forms.CharField(max_length=75,null=True,blank=True)

class CommentaryForm(forms.Form):
    commentary = forms.CharField(max_length=256)
    user = forms.ModelChoiceField(queryset= User.objects.all())

class QueryForm(forms.Form):
    user = forms.ModelChoiceField(queryset= User.objects.all())
    query = forms.CharField(max_length=256)

class Customizable(forms.Form):
    user = forms.ModelChoiceField(queryset= User.objects.all())
    image = forms.ImageField()
    description = forms.CharField(max_length=256, null=True, blank=True)
    phone = forms.CharField(null=True, blank=True)
    area_code = forms.CharField(max_length=9)


class Bought(forms.Form):
    user = forms.ModelChoiceField(queryset= User.objects.all())
    direction = forms.CharField(max_length = 256)
    direction_number = forms.IntegerField()
    cp = forms.IntegerField(max_length = 32)
    date = forms.DateTimeField()

class ProductBougth(forms.Form):
    Bought = forms.ModelChoiceField(queryset = Bought.objects.all())
    name = forms.CharField(max_length=64)
    category = forms.ModelChoiceField(queryset= Category.objects.all())
    price = forms.IntegerField()
    amount = forms.IntegerField(blank = True, null=True, default=1)
    accumulated = forms.IntegerField()

class SingUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
        help_texts = {k:'' for k in fields}


class UserEditForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
        help_texts = {k:'' for k in fields}
