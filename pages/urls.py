from django.urls import path
from .views import HomePageView, AboutPageView, Categories

urlpatterns = [
    path('categories/', Categories.as_view(), name='categories'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
]
