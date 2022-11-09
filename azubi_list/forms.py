from django import forms

class SearchForm(forms.Form):
    search_input = forms.CharField(label='Suche', max_length=100)