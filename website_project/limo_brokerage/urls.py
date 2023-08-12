from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_limo_data, name='limo_list'),
    path('<int:id>/', views.get_limo_detail, name='limo_detail'),
]