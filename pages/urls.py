
from django.urls import path
from pages.views import HomePageView,AboutPageView,contactPageView,services

urlpatterns = [
    path('',HomePageView.as_view()),
    path('about/',AboutPageView.as_view()),
    path('contact/',contactPageView.as_view()),
    path( 'services/',services)
]
