from rest_framework.permissions import BasePermission
from  .models  import companies,employers
class companyPermission(BasePermission):
    
    def has_permission(self, request, view):
       try:
           
        client_id=request.data.get('company_id')
        email=request.session['username']
        user=companies.objects.get(email=email)
        
       
        request.session['id']=user.company_id
        if str(user.company_id)==client_id:
          return True
        else:
            return False
       except companies.DoesNotExist: 
           return False

class employerPermission(BasePermission):
    def has_permission(self, request, view):
        try:
            client_id=request.data.get('emp_id')
            email=request.session['username']
            user=employers.objects.get(email=email)
            
            request.session['id']=user.emp_id                #for future use
            if str(user.emp_id)==client_id:
               return True
            else:
               return False
        except employers.DoesNotExist: 
            return False

class employerGetPermission(BasePermission):
    def has_permission(self, request, view):
      if request.method=='GET':
        try:
            client_id=request.data.get('emp_id')
            email=request.session['username']
            user=employers.objects.get(email=email)
            
            request.session['id']=user.emp_id                #for future use
            if str(user.emp_id)==client_id:
               return True
            else:
               return False
        except employers.DoesNotExist: 
            return False
      else:
          return False                  
