
from django.urls import path
from shopp import views
from django.conf import settings
from django.conf.urls.static import static
    

urlpatterns = [
    path('',views.shop, name = "shop"),
]
