from django.contrib import admin
from .models import *

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
  
    def active(self, obj):
        return obj.is_active == 1
  
    active.boolean = True
admin.site.register(Blog, BlogAdmin)