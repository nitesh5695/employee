from rest_framework.permissions import BasePermission
from .backend  import MyAuthentication
from  .models  import companies,employers
class companyPermission(BasePermission):
    
    def has_permission(self, request, view):
      email=request.session['username']
      is_employee=MyAuthentication.isemployee(email)
      if(is_employee):
          if request.method=='GET':
              return True
          else:
              return False 
      else:
          return True

class employerPermission(BasePermission):
    def has_permission(self, request, view):
        
        email=request.session['username']
        is_employee=MyAuthentication.isemployee(email)
        if(is_employee):
            if request.method=='GET' or request.method=='POST':
                return True
            else:
                return False 
        elif request.method=='GET' or request.method=='PATCH' or request.method=='DELETE':
            return True
        else:
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
