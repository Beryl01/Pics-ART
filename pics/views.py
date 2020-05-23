from django.http import HttpResponse, Http404
from .models import Image, Location, Category
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'index.html')

def gallery(request):
    image = Image.objects.all()
    return render(request, 'images.html', {"image": image})

def location(request):
    image = Image.objects.all()
    locations = Location.objects.all()
    return render(request, 'location.html', {"image": image, "locations": locations})    

def search_by_location(request, location):
    locations = Location.objects.all()
    image = Image.search_by_location(location)
    return render(request, 'location.html', {"image": image, "locations": locations})        

def search_results(request):
    if 'searchItem' in request.GET and request.GET["searchItem"]:
        search_term = request.GET.get("searchItem")
        searched_image = Image.search_by_category(search_term)
        message = f"{search_term}"
        return render(request, 'search.html', {"message": message, "image": searched_image})
    else:
        message = "search term"
        return render(request, 'search.html', {"message": message})

    



