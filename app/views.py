from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Hood, Location
from .forms import HoodForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout




# Create your views here.

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try: 
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'user doesnt exist')

        user = authenticate(request, username= username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or password does not exist')

    context = {

    }
    return render(request, 'app/login_register.html', context)

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
