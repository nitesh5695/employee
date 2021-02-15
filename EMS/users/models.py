from django.db import models
from django.db.models.enums import Choices

class companies(models.Model):
    company_id=models.AutoField(primary_key=True)
    company_email=models.CharField(max_length=300,unique=True)
    password=models.CharField(max_length=200,null=False)
    company_name=models.CharField(max_length=300,null=False)
    def __str__(self):
        return self.company_email

class company_profile(models.Model):
    company_id=models.OneToOneField(companies,on_delete=models.CASCADE)
    address=models.CharField(max_length=600)
    established_year=models.CharField(max_length=4)
    ceo=models.CharField(max_length=100)
    contact_no=models.CharField(max_length=13)
    gst_no=models.CharField(max_length=100)
    created_at=models.DateField(auto_now_add=True,blank=True)


class employers(models.Model):
    emp_id=models.AutoField(primary_key=True)
    email=models.EmailField(max_length=300,unique=True)
    name=models.CharField(max_length=250,null=True)
    password=models.CharField(max_length=200,null=True)
    company_id=models.CharField(max_length=300,null=True)
    
    def __str__(self):
        return self.email

class employer_profile(models.Model):
    emp_id=models.OneToOneField(employers,on_delete=models.CASCADE,primary_key=True)
    dob=models.DateField()
    choice=(
        ("male","Male"),
        ("female","Female"),
        ("others","others")
    )
    gender=models.CharField(max_length=10,choices=choice)
    address=models.CharField(max_length=600,blank=True)
    mobile_no=models.CharField(max_length=13,blank=True)
    joining_date=models.DateField()
    company_id=models.CharField(max_length=10,null=True)
    project_id=models.CharField(max_length=10)
    department_id=models.CharField(max_length=10,null=True)
    created_at=models.DateField(auto_now_add=True)





