from django import forms
from django.forms import ModelForm, TextInput, EmailInput, DateInput, SelectDateWidget
from .models import Azubi, Profession


class FormDateInput(forms.DateInput):
    input_type = 'date'
class SearchForm(forms.Form):
    search_input = forms.CharField(label='Suche', max_length=100)

class DeleteForm(forms.Form):
    hidden_input = forms.CharField(max_length=0)


class AzubiForm(ModelForm):
    class Meta:
        model = Azubi
        fields = '__all__'
        widgets = {
            'first_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Vorname'
                }), 
             'last_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Nachname'
                }), 
            'email': EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                }), 
            'birthday': FormDateInput( attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Geburtstag(YYYY-MM-DD)'
                }),
            'address': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Addresse'
                }), 
             'PLZ': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'PLZ'
                }), 
            'department': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Abteilung'
                }), 
            'year': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Ausbildungsjahr'
                }), 
            'phone_number': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Telefonnummer'
                }), 
            }
           
class ProfessionForm(ModelForm):
    class Meta:
        model = Profession
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Beruf'
                })
        }