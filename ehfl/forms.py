
from django import forms

class MenuPreferencesForm(forms.Form):
    calories_per_day = forms.IntegerField()
    low_sodium = forms.BooleanField(required=False)
    low_sugar = forms.BooleanField(required=False)
    high_fiber = forms.BooleanField(required=False)
    budget = forms.FloatField()
    address = forms.CharField(max_length=160)
