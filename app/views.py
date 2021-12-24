from django.shortcuts import render
from .models import Hood



# Create your views here.

def home(request):
    hoods = Hood.objects.all()
    context = {
        'hoods':hoods
    }
    return render(request, 'app/home.html', context)

    


def hood(request, pk):
    hood = Hood.objects.get(id=pk)    
    context = {
        'hood':hood
    }
    return render(request, 'app/hood.html', context)
