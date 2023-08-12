from django.urls import path
from . import views

app_name = 'lead_generation'

urlpatterns = [
    path('leads/', views.get_lead_data, name='lead_list'),
    path('leads/capture/', views.submit_lead_capture_form, name='lead_capture'),
]