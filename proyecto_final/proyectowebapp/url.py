
from django.urls import path
from proyectowebapp import views

    

urlpatterns = [
    path('home/', views.home, name="home"),
    path('services/',views.services, name="service"),
    path('shop/',views.shop,name="shop"),
    path('blog/',views.blog, name= "blog"),
    path('contacus/', views.contacus, name = "contacus"),
]