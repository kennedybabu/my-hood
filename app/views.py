from django.shortcuts import render



# Create your views here.


hoods = [
    {'id':1, 'name':'buruburu '},
    {'id':2, 'name':'kitengela'},
    {'id':3, 'name':'kiambu'}
]


def home(request):
    return render(request, 'app/home.html', {'hoods':hoods})


def hood(request, pk):
    hood = None
    for i in hoods:
        if i['id']== pk:
            hood = i

    context = {
        'hood':hood
    }
    return render(request, 'app/hood.html', context)
