from django.shortcuts import render
from rest_framework import viewsets , generics
from api.models import Company
from api.serializers import CompanySerializers
# Create your views here.

# class CompanyViewSet(viewsets.ModelViewSet):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializers
    

class CompanyName(generics.ListCreateAPIView):
    serializer_class = CompanySerializers

    def get_queryset(self):
        queryset = Company.objects.all()
        Company = self.request.query_params.get('Company')
        if CompanyName is not None:
            queryset = queryset.filter(CompanyName__icontains=Company)

        return queryset()
    
class CompanyAbout(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers

class CompanyLocation(generics.ListAPIView):
    serializer_class = CompanySerializers
    queryset = Company.objects.all()
