from django import forms

class SearchForm(forms.Form):
    search_input = forms.CharField(label='Suche', max_length=100)

# class FormName(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     text = forms.CharField(widget=forms.Textarea)
