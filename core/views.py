from django.shortcuts import render
from django.http import HttpResponse
from core.forms import NumberForm
import math

# Create your views here.
def index(request):
    if request.method == 'POST':
        
        form = NumberForm(request.POST)
        
        if form.is_valid():
            numero = int(form.cleaned_data['number_field'])
            expoente=0
            numero_convertido = 0
            while(numero > 0):
                digito = numero % 10 # pegar o ultimo digito do numero
                numero = int(numero / 10)
                numero_convertido += digito * pow(2,expoente)
                expoente = expoente + 1
            context = {
                'form': form,
                'numero_convertido':numero_convertido
            }     
            return render(request, 'index.html',context=context)

    else:
        form = NumberForm()
    
    context = {
        'form': form
    }     
    return render(request, 'index.html', context=context)