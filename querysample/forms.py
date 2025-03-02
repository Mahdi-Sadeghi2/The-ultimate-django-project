from django import forms
from django.forms import TextInput, Select,modelform_factory

from .models import Employees


class CountriesForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = "__all__"

        widgets = {'first_name': TextInput(
            attrs={'class': "form-control", 'style': "max-width:300px;", 'palceholder': 'First name'}), 'last_name': TextInput(
            attrs={'class': "form-control", 'style': "max-width:300px;", 'palceholder': 'Last name'}), 'country': Select(
            attrs={'class': "form-control", 'style': "max-width:300px;", 'palceholder': 'Country'}), 'stae': Select(
            attrs={'class': "form-control", 'style': "max-width:300px;", 'palceholder': 'State'}), 'City': Select(
            attrs={'class': "form-control", 'style': "max-width:300px;", 'palceholder': 'City'})}
