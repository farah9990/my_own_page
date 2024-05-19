from django import forms

class SearchForm(forms.Form):
    q = forms.CharField(
        widget=forms.TextInput(attrs={
            'id': 'textInput',
            'placeholder': 'Enter your search query...',
            'list': 'list'
        })
    )