from django.shortcuts import render
from django.views import View
from core.forms import NumberForm

class NumberView(View):
    def get(self, request, *args, **kwargs):
        form = NumberForm()
        return render(request, 'index.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = NumberForm(request.POST)
        if form.is_valid():
            if(len(str(form.cleaned_data['number_field'])) >= 10):
                converted_number = get_larger_number_converted( int(form.cleaned_data['number_field']) )
            else:
                converted_number = get_number_converted( int(form.cleaned_data['number_field']) )
        else:
            converted_number = None
            
        return render(request, 'index.html', {'form': form, 'numero_convertido': converted_number})

def get_number_converted(numero):
    expoente=0
    numero_convertido = 0

    while(numero > 0):
        digito = numero % 10 
        numero = int(numero / 10)
        numero_convertido += digito * pow(2,expoente)
        expoente = expoente + 1
    
    return numero_convertido

def get_larger_number_converted(numero):
    k = 0
    while(True):
        if (int(numero / pow(10,k)) == numero % pow(10,k)):
            break
        k = k + 1
              
    part_one = get_number_converted(pow(10,k))
    part_two = get_number_converted(int(numero / pow(10,k)))
    
    return part_one + part_two      
