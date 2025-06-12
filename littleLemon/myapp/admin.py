from django.contrib import admin
from .models import Menu, Booking

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'inventory')
    search_fields = ('name',)
    
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'booking_date', 'no_of_guests')
    search_fields = ('name',)
    
admin.site.register(Menu, MenuAdmin)
admin.site.register(Booking, BookingAdmin)