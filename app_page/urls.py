from django.urls import path
from .views import HomePageView, AboutPageView, AboutMePageView

urlpatterns = [
    path('about/about_me/', AboutMePageView.as_view(), name='about_me'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
]