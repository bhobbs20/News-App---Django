from django.shortcuts import render, get_object_or_404, redirect
from .models import Main


def home(request):
    title = Main.objects.all()
    
    context = {
        'title': title,
    }
    return render(request, 'home.html', context)