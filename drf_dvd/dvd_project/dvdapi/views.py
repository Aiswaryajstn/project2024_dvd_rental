from django.shortcuts import render
from rest_framework import generics

from .serializer import ActorSerializer
from .models import Actor

class ActorListAPIView(generics.ListAPIView):
   queryset = Actor.objects.all() 
   serializer_class = ActorSerializer
   