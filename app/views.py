from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Hood, Location
from .forms import HoodForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')


    if request.method == 'POST':
        username = request.POST.get('username').lower()
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
        'page':page
    }
    return render(request, 'app/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerUser(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')
    context = {
        'form':form
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


@login_required(login_url='login')
def createHood(request):
    form = HoodForm()
    if request.method == 'POST':
        form = HoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'app/hood_form.html', context)


@login_required(login_url='login')
def updateHood(request, pk):
    hood = Hood.objects.get(id=pk)
    form = HoodForm(instance=hood)

    if request.user != hood.host:
        return HttpResponse('You are not allowed')

    if request.method == 'POST':
        form = HoodForm(request.POST, instance=hood)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form':form
    }
    return render(request, 'app/hood_form.html', context)



@login_required(login_url='login')
def deleteHood(request, pk):
    hood = Hood.objects.get(id=pk)

    if request.user != hood.host:
        return HttpResponse('You are not allowed')

    if request.method == 'POST':
        hood.delete()
        return redirect('home')
    context = {

    }
    return render(request, 'app/delete.html', {'obj':hood})
