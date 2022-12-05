from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cars/', views.cars, name='cars'),
    path('cars/<int:id>/car-details/', views.car_details, name='car_details'),
    path('about/', views.about_us, name='about'),
    path('about/blog/', views.blog, name='blog'),
    path('about/blog/blog-details/', views.blog_details, name='blog_details'),
    path('about/team/', views.team, name='team'),
    path('about/testimonials/', views.testimonials, name='testimonials'),
    path('about/faq/', views.faq, name='faq'),
    path('about/terms/', views.terms, name='terms'),
    path('contact/', views.contact, name='contact'),
]
