from django.urls import path
from .views import CreateLocationView, RetrieveLocationView

urlpatterns = [
    path('create/', CreateLocationView.as_view(), name='create-location'),
    path('', RetrieveLocationView.as_view(), name='retrieve-locations'),
]
