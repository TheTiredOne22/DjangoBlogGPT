from .views import ChatHomeView
from django.urls import path


urlpatterns = [
    path('', ChatHomeView.as_view(), name='index')
]
