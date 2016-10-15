from django.contrib import admin
from models import Webuser

# Register your models here.

@admin.register(Webuser)
class WebuserAdmin(admin.ModelAdmin):
    pass
