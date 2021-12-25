from django.shortcuts import render, redirect
from .models import Hood, Location
from .forms import HoodForm
from django.db.models import Q



# Create your views here.

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    hoods = Hood.objects.filter(Q(location__name__icontains=q) | Q(name__icontains=q))
    locations = Location.objects.all()
    hood_count = hoods.count()

    context = {
        'hoods':hoods,
        'locations':locations,
        'hood_count':hood_count
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
