from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from petapi.views import CityView,  PetView, PostView

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'cities', CityView, 'city')
router.register(r'pets', PetView, 'pet')
router.register(r'posts', PostView, 'post')

urlpatterns = [
    path('', include(router.urls)),
]

