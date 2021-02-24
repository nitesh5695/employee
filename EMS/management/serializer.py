from rest_framework import  serializers
from .models import Department, Leave,Project,Salary

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model=Leave
        fields="__all__"
class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model=Salary
        fields="__all__"   

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields="__all__"
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields="__all__"
        exclude=('request')