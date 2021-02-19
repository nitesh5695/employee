from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .JWTTokens import *
from .JWTTokenAuthentication import JWTAuthentication
from .permissions import companyPermission,employerPermission
from .backend  import MyAuthentication
from .models import employers,employer_profile,companies,company_profile
from  .serializer import companySerializer,employerSerializer,company_profileSerializer, employer_profileSerializer,employer_profileSerializer

class gettoken(APIView):
    def post(self,request):
        email=request.data.get('email')
        password=request.data.get('password')
        user=MyAuthentication.authenticate(request,email=email,password=password)
        if user is not None:
            
            access=access_token(user)
            refresh=refresh_token(user)
            MyAuthentication.login(request,user.email)
        return Response({'user':user.email,'access':access,'refresh':refresh})

class company_register(APIView):
    authentication_classes=[JWTAuthentication]
    def post(self,request):
        serializer=companySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'registered'})
        return Response(serializer.errors)  
    def get(self,request):
        email=request.session['username']
        data=companies.objects.get(email=email)  
        serializer=companySerializer(data)
        return Response(serializer.data) 
class company_pofile(APIView):
    # authentication_classes=[JWTAuthentication]
    # permission_classes=[companyPermission]
    def get(self,request):
        data=company_profile.objects.get()
        serializer=company_profileSerializer(data)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer=company_profileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'saves successfully'})
        return Response(serializer.errors)    

class employer_register(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[companyPermission]
    def post(self,request):
        serializer=employerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'registered'})
        return Response(serializer.errors)
       
class employer_profile(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[companyPermission]
    def post(self,request):
        serializer=employer_profileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'saved successfully'})
        return Response(serializer.errors)           
