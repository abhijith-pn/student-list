from rest_framework import serializers

from .models import College, Student


class CollegeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = College
        fields = ('id', 'url', 'name')


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'url', 'name', 'gpa', 'college')
