from django.contrib import admin
from .models import MenuItem, Reserva
from django.contrib import admin
from rest_framework.authtoken.models import Token

admin.site.register(Token)
# Register your models here.
admin.site.register(MenuItem)
admin.site.register(Reserva)