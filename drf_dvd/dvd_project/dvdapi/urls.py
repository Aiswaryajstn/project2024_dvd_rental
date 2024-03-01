from django.urls import path
from . import views


urlpatterns = [
   path('', views.ActorListAPIView.as_view())
]