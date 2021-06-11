from django import forms

class HomeForm(forms.Form):
    gnre=forms.CharField(label='gnre', max_length=100)
    language=forms.CharField(label='language', max_length=10)
    

    