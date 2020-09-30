from django.urls import path 
from main import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name = 'about'),
    path('base/', views.base, name = 'base'),
    path('services/', views.services, name = 'services'),
    path('trainings/', views.trainings, name = 'trainings'),
    path('contact/', views.contact, name = 'contact'),
    path('application/', views.application, name = 'application'),
    path('blog', views.blog, name = 'blog'),
]
