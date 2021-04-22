
from django.urls import path
from proyectowebapp import views
from django.conf import settings
from django.conf.urls.static import static
    

urlpatterns = [
    path('home/', views.home, name="home"),
    path('shop/',views.shop,name="shop"),
    path('blog/',views.blog, name= "blog"),
    path('contacus/', views.contacus, name = "contacus"),
]

urlpatterns+= static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
