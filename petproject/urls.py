from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from petapi.views import (
    PostViewSet,
    UserViewSet,
    TypeViewSet,
    PetViewSet,
    CityViewSet,
)

router = DefaultRouter(trailing_slash=False)

router.register(r'cities', CityViewSet, 'city')
router.register(r'pets', PetViewSet, 'pet')
router.register(r'posts', PostViewSet, 'post')
router.register(r"users", UserViewSet, basename="users")
router.register(r"types", TypeViewSet, basename="type")

urlpatterns = [
    path('', include(router.urls)),
    path("login", UserViewSet.as_view({"post": "user_login"}), name="login"),
    path(
        "register", UserViewSet.as_view({"post": "register_account"}), name="register"
    ),
]

