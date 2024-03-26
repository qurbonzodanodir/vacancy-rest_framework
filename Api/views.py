from rest_framework import generics
from rest_framework.response import responses
from .serializer import *
from rest_framework import permissions
from .models import *

class CategoryCreateApi(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)

class CompanyCreateApi(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = {permissions.IsAuthenticatedOrReadOnly}

class VacancyCreateApi(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = {permissions.IsAuthenticatedOrReadOnly}


class VacancyRetrieveApi(generics.RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = {permissions.IsAuthenticatedOrReadOnly}

class VacancyListApi(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = {permissions.IsAuthenticatedOrReadOnly}

class ApplicationsCreateApi(generics.CreateAPIView):
    queryset = Applications.objects.all()
    serializer_class = ApplicationsSerializer
    permission_classes = {permissions.IsAuthenticatedOrReadOnly}

class ApplicationsListApi(generics.ListAPIView):
    queryset = Applications.objects.all()
    serializer_class = ApplicationsSerializer
    permission_classes = {permissions.IsAuthenticatedOrReadOnly}

    


