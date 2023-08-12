from django.contrib import admin
from .models import Limo, Tracking

class LimoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'availability', 'location')
    search_fields = ('name', 'description')
    list_filter = ('availability',)

class TrackingAdmin(admin.ModelAdmin):
    list_display = ('id', 'limo_id', 'current_location')
    search_fields = ('limo_id',)

admin.site.register(Limo, LimoAdmin)
admin.site.register(Tracking, TrackingAdmin)