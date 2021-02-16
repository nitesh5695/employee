from django.shortcuts import render
from rest_framework import serializers
from .models import companies,employers
from rest_framework.views import APIView
from rest_framework.response import Response
from .JWTTokens import *
from .backend  import MyAuthentication
from .models import employers,employer_profile,companies,company_profile
from  .serializer import companySerializer,employerSerializer

class gettoken(APIView):
    def post(self,request):
        email=request.data.get('email')
        password=request.data.get('password')
        user=MyAuthentication.authenticate(request,email=email,password=password)
        if user is not None:
            access=access_token(user)
            refresh=refresh_token(user)
        return Response({'user':user.email,'access':access,'refresh':refresh})

class login(APIView):
    def post(self,request):
        user=MyAuthentication.authenticate(self,request,username="nit@gmail.com",password="nitesh5695")
        request.user=user 

        return Response({'message':str(request.user)})

class company_register(APIView):
    def post(self,request):
        serializer=companySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'registered'})
        return Response(serializer.errors)  
class employer_register(APIView):
    def post(self,request):
        serializer=employerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'registered'})
            
        return Response(serializer.errors)