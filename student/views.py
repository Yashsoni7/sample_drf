from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import student, GENDER
from .serializers import StudentSerializer

#View for Student
class StudentList(APIView):

    #Get Request to fetch all students name
    def get(self,request, format=None):
        students = student.objects.all()
        serializer = StudentSerializer(students ,many=True)
        return Response(serializer.data)

    #Post request to post a new student in the API
    def post(self,request,format=None):
        serializer = StudentSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)