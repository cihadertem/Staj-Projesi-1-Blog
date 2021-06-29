from django.shortcuts import render, HttpResponse

def home_view(request):
    if request.user.is_authenticated:
        context = {
        'isim': 'Cihad',
    }
    else:
        context = {
        'isim' : 'Misafir',
    }
    return render(request, 'home.html', context)
# Create your views here.
