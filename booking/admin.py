from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

admin.site.unregister(Group)

class servicesAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Service Details', {
            'fields': ('title', 'photo', 'description', 'location', 'category', 'slug')
        }),

        ('Pricing', {
            'fields': ('service_1', 'price_1',)
        }),)

    list_display = ('title', 'location', 'category')
  
    def active(self, obj):
        return obj.is_active == 1
  
    active.boolean = True
admin.site.register(services, servicesAdmin)

admin.site.register(contact)

class bookAdmin(admin.ModelAdmin):
    list_display = ('user', 'services_required', 'date', 'time')
  
    def active(self, obj):
        return obj.is_active == 1
  
    active.boolean = True
admin.site.register(book, bookAdmin)

admin.site.register(Category)
admin.site.register(Location)
