from django.urls import re_path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from testdemo import views
from django.conf import settings
from django.conf.urls.static import static
router = DefaultRouter()
#router.register(r'dit', views.parentViewViewset)
#router.register(r'users', views.UserViewSet)


urlpatterns = [

    
    re_path(r'^login/$', views.LoginViews.as_view(), name='login'),
    re_path(r'^home/$', views.homeViews.as_view(), name="home"),
    re_path(r'^delete/$', views.deleteList, name="delete"),
    re_path(r'^edit/$', views.updateHome.as_view(), name="edit"),


    re_path(r'^employeeList/$', views.EmployeeView.as_view(), name="employeeList"),
   

    
]
