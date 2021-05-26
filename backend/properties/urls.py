from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(
    "properties",
    views.PropertiesViewSet,
)

app_name = "properties"
urlpatterns = [path("", include(router.urls))]


