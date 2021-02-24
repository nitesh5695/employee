
from django.contrib import admin
from django.urls import path
from users import views
from management import views as mviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new_user/',views.newuser.as_view()),
    path('gettoken/',views.gettoken.as_view()),
    #path('refreshtoken/',views.refreshtoken.as_view()),
    path('company_register/',views.company_register.as_view()),
    path('company_profile/',views.company_pofile.as_view()),
    path('employer_register/<int:pk>/',views.employer_register.as_view()),
    path('employer_register/',views.employer_register.as_view()),
    path('employer_profile/',views.employer_profiles.as_view()),
    path('employer_profile/<int:pk>/',views.employer_profiles.as_view()),
    path('projects/<int:pk>/',mviews.projects.as_view()),
    path('projects/',mviews.projects.as_view()),
    path('leaves/',mviews.leaves.as_view())
]
