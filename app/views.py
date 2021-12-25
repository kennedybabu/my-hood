from django.shortcuts import render, redirect
from .models import Hood
from .forms import HoodForm



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

def createHood(request):
    form = HoodForm()
    if request.method == 'POST':
        form = HoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'app/hood_form.html', context)


def updateHood(request, pk):
    hood = Hood.objects.get(id=pk)
    form = HoodForm(instance=hood)

    if request.method == 'POST':
        form = HoodForm(request.POST, instance=hood)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form':form
    }
    return render(request, 'app/hood_form.html', context)


def deleteHood(request, pk):
    hood = Hood.objects.get(id=pk)
    if request.method == 'POST':
        hood.delete()
        return redirect('home')
    context = {

    }
    return render(request, 'app/delete.html', {'obj':hood})
