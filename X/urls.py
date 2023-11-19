from django.urls import path
from .views import HomePageView, Temp

urlpatterns = [
    path('', HomePageView, name='home'),
    path('X/', Temp.as_view(), name='about'),
]