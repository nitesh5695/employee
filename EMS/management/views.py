
from django.shortcuts import render
from rest_framework import status
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from users.JWTTokens import *
from users.JWTTokenAuthentication import JWTAuthentication
from users.permissions import companyPermission,employerPermission
from users.backend  import MyAuthentication
from users.models import employers,employer_profile,companies,company_profile
from  users.serializer import companySerializer,employerSerializer,company_profileSerializer, employer_profileSerializer,employer_profileSerializer
from .serializer import SalarySerializer,ProjectSerializer,LeaveSerializer,DepartmentSerializer
from .models import Leave, Project,Department,Salary

class projects(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[companyPermission]
    def get(self,request):
      try:  
        company_id=request.session['company_id']
        all_project=Project.objects.filter(company_id=company_id)
        serializer=ProjectSerializer(all_project,many=True)
        return Response(serializer.data)
      except Exception as e:
        print(e)
        return Response({'message':'You have no company'})  

    def post(self,request):
        request.data['company_id']=request.session['company_id']
        serializer=ProjectSerializer(data=request.data)    
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Project added'})
        return Response(serializer.errors)    
    def put(self, request,pk=None):
        id =pk
        project = Project.objects.get(project_id=id)
        serializer = ProjectSerializer(project,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

    def patch(self, request,pk=None):
        id =pk
        project = Project.objects.get(project_id=id)
        serializer = ProjectSerializer(project,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    def delete(self, request, pk, format=None):
        id = pk
        project = Project.objects.get(project_id=id)
        project.delete()
        return Response({'message':'Project Deleted'})        

class leaves(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[employerPermission]
    # def get(self,request,pk=None):
    #     id=pk
    #     if id is None:
    #       data=Leave.objects.filter(emp_id=1)
    #       for x in data:
    #           print(x.emp_id.name)
    #       return Response({'message':"run"})
    def post(self,request):
        request.data['emp_id']=request.session['emp_id']
        serializer=LeaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'request done'})      
        return Response({serializer.errors})
    def patch(self,request,pk=None):
        emp_id=pk
        data1=Leave.objects.filter(emp_id=emp_id)    
        serializer=LeaveSerializer(data1,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'updated'})
        return Response(serializer.errors)   
    def delete(self,request,pk=None): 
        leave_id=pk
        emp_id=request.session['emp_id']
        leave_obj=Leave.objects.get(leave_id=id,emp_id=emp_id)    
        leave_obj.delete()
        return Response({'message':'deleted successfully'})

class all_departments(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[companyPermission]
    def get(self,request):
        all_department=Department.objects.all()
        serializer=DepartmentSerializer(all_department)
        return Response(serializer.data)   
    def post(self,request):
        serializer=DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'requested successfully'})  
        return Response(serializer.errors)     

class salary(APIView):
    def get(self,request,pk=None):
        all_salaries=Salary.objects.filter(emp_id=pk)
        serializer=SalarySerializer(all_salaries)
        return Response(serializer.data)

    def post(self,request):
        serializer=SalarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'salary paid successfully'})
        return Response(serializer.errors)

    #                





