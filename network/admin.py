from django.contrib import admin
from .models import User, Advisor, BookedCalls

# Register your models here.

admin.site.register((User,Advisor,BookedCalls))
