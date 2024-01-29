from django.contrib import admin
from .models import List

# Register your models here.

class ListAdmin(admin.ModelAdmin):
    list_display = ("list_context","pub_date","complete")
admin.site.register(List,ListAdmin)