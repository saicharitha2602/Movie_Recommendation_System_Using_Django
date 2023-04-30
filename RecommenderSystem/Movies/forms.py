from django.forms import forms, ModelChoiceField
from .models import User, Category, Movie, SearchHistory
from django import forms
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = "__all__"

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields="__all__"

class MovieForm(forms.ModelForm):
    
    class Meta:
        model=Movie
        exclude=("Genre_name",)

