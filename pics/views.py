from django.http import HttpResponse, Http404
from .models import Image, Location, Category
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'index.html')

def gallery(request):
    image = Image.objects.all()
    return render(request, 'images.html', {"image": image}) 



