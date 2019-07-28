from django.urls import path

from .views import BuildingsList, FilesList


urlpatterns = [
    path('', BuildingsList.as_view(), name='BuildingsList'),
    path('files/', FilesList.as_view(), name='FilesList'),
]
