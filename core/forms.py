from xml.dom import ValidationErr
from django import forms

class NumberForm(forms.Form):
    number_field = forms.IntegerField(label='Digite um numero binario')


    def clean(self):
        if self.cleaned_data['number_field'] > 8:
            raise forms.ValidationError('Numero não pode ter mais de 8 numeros')

    
