from email.policy import default
from xml.dom import ValidationErr
from django import forms

class NumberForm(forms.Form):
    number_field = forms.IntegerField()
    
    def clean(self):
        errors = {}
        aux = self.cleaned_data['number_field']
        while(aux > 0):
            if(aux % 10 != 0 and aux % 10 != 1):
                errors['number_field'] = "Apenas digitos binarios são aceitos."
                break
            aux = int(aux / 10)        
        if len(str(self.cleaned_data['number_field'])) > 8:
            errors['number_field'] = "Numero não pode ter mais de 8 digitos."
        
        if errors:
            raise forms.ValidationError(errors)
        

    
