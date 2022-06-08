from django.shortcuts import render

# Create your views here.

def store(request):
    context = {}
    return render(request, 'store/store.html', context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

def iniciar_sesion(request):
    context = {}
    return render(request, 'store/login.html', context)

def registrarse(request):
    context = {}
    return render(request, 'store/registrarse.html', context)

