from django import forms

class DeloForm(forms.Form):
    delo = forms.CharField()