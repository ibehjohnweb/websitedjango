from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('home.html', views.home, name='home'),
    path('contact.html', views.contact, name='contact'),
    path('about.html', views.about, name='about'),
    path('dj.html', views.dj, name='dj'),
    path('bookings.html', views.bookings, name='bookings'),
    path('ee.html', views.engineering, name='engineering'),
    path('web.html', views.web, name='web'),
]


