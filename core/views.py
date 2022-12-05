from django.shortcuts import render, get_object_or_404
from .models import Car

# Create your views here.
def index(request):
    featured_cars = Car.objects.filter(featured=True)
    return render(request, 'index.html', {'featured_cars': featured_cars})

def cars(request):
    cars = Car.objects.filter(available=True)
    return render(request, 'cars.html', {'cars': cars})

def car_details(request, id):
    car = get_object_or_404(Car, id=id, available=True)
    return render(request, 'car-details.html', {'car': car})

def about_us(request):
    return render(request, 'about-us.html')

def blog(request):
    return render(request, 'blog.html')

def blog_details(request):
    return render(request, 'blog-details.html')

def team(request):
    return render(request, 'team.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def faq(request):
    return render(request, 'faq.html')

def terms(request):
    return render(request, 'terms.html')

def contact(request):
    return render(request, 'contact.html')