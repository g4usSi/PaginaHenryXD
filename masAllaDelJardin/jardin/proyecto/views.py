from django.shortcuts import render

# Create your views here.

def proyecto_view(request):
    return render(request, 'proyecto.html')