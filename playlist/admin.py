from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_published', )
    list_editable = ('is_published', )