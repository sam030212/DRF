from django.contrib import admin
from django.urls import path, include
#from api.views import CompanyViewSet
from rest_framework import routers
from .views import CompanyName, CompanyAbout, CompanyLocation



# router = routers.DefaultRouter()
# router.register(r'companies', CompanyViewSet)


urlpatterns = [
    
    path('cname/',CompanyName.as_view()),
    path('about/<int:pk/>',CompanyAbout.as_view()),
    path('location/',CompanyLocation.as_view()),
    #path('company/',CompanyName.as_view,()),


]
