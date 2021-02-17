from django.db import models
import datetime

from users.models import companies, employers


class Department_cmpid(models.Model):
    dept_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(companies, on_delete=models.CASCADE)

employers
choice = (
    ('accept', 'accept'),
    ('reject', 'reject')
)
class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    department = models.ForeignKey(Department_cmpid, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=100)
    request = models.CharField(max_length = 10, choices=choice, default = 'reject')

    def __str__(self):
        return self.department_name

class LeaveType(models.Model):
    leave_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255, default='Annual Leave')

    def __str__(self):
        return self.type


class Leave(models.Model):
    leave_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(employers, on_delete=models.CASCADE)
    type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    from_date = models.DateField(default=datetime.date.today)
    to_date = models.DateField(default=datetime.date.today)
    reason = models.TextField(max_length=1200, default='Not Feeling Well')
    status = models.CharField(max_length=10, choices=choice, default='reject')


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)

class Salary(models.Model):
    salary_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(employers, on_delete=models.CASCADE)
    from_date = models.DateField(auto_now_add=True,blank=True)
    to_date = models.DateField(auto_now_add=True,blank=True)
    salary = models.IntegerField()
