from django.contrib import admin
from .models import service


class Adminservice(admin.ModelAdmin):
    readonly_fields=('created','update')
# Register your models here.
admin.site.register(service,Adminservice)