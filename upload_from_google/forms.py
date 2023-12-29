from django import forms
from django.core import validators

class GoogleTableForm(forms.Form):
    url = forms.URLField(max_length=200, label='Адрес гугл-таблицы с данными')
    desired_sheets = forms.CharField(max_length=200, label='Список листов через запятую')
