from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('limos/', include('limo_brokerage.urls')),
    path('leads/', include('lead_generation.urls')),
]