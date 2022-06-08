from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='inicio'),
    path('carro', views.cart, name='carro'),
    path('checkout', views.checkout, name='compra'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('iniciar_sesion', views.iniciar_sesion, name='iniciar_sesion'),
]