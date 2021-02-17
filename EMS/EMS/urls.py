
from django.contrib import admin
from django.urls import path, include
from users import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', include('employee.urls')),

    path('gettoken/',views.gettoken.as_view()),
    #path('refreshtoken/',views.refreshtoken.as_view()),
    path('company_register/',views.company_register.as_view()),
    path('company_profile/',views.company_profile.as_view()),
    path('employer_register/',views.employer_register.as_view()),
    path('employer_profile/',views.employer_profile.as_view()),

]
