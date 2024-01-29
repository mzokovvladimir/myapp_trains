from django import forms

from cities.models import City


class HtmlForm(forms.Form):
    name = forms.CharField(label='Місто')


class CityForm(forms.ModelForm):
    name = forms.CharField(label='Місто', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введіть назву міста'
    }))

    class Meta:
        model = City
        fields = ('name', )

