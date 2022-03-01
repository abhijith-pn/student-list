from django.shortcuts import render
from rest_framework import viewsets

from .models import College, Student
from .serializers import CollegeSerializer, StudentSerializer

# Create your views here.
class CollegeApiView(viewsets.ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer

class StudentApiView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
