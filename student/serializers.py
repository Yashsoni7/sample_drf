from rest_framework import serializers
from .models import student,GENDER

#Serializer for Student
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = ['stdid','name','age','std','gender']