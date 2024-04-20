from django.urls import path
from.import views
urlpatterns = [
    path('', views.proyecto_view, name = 'proyecto'),
    
]