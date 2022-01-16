from django.shortcuts import render
from django.http import HttpResponse
from core.forms import NumberForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        
        form = NumberForm(request.POST)
        
        if form.is_valid():
            context = {
                'form': NumberForm()
            }     
            return render(request, 'index.html',context=context)

    else:
        form = NumberForm()
    
    context = {
        'form': form
    }     
    return render(request, 'index.html', context=context)