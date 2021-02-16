
from .models import companies,employers
from rest_framework import exceptions
class MyAuthentication():
    def authenticate(request,email=None, password=None):    
        try:
            user= employers.objects.get(email=email,password=password)
        except employers.DoesNotExist:
            try:
                print(" company")
                user=companies.objects.get(email=email,password=password)
            except:
                raise exceptions.AuthenticationFailed('email or password is wrong')    
            request.session['username']=user.email
            return user
           
        except companies.DoesNotExist:
            print("not exist")
            return None
        except Exception as e:
            print("not exist1")
            
            return None
            