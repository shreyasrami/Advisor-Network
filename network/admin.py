from django.contrib import admin
from .models import User, Advisor

# Register your models here.

admin.site.register((User,Advisor))
