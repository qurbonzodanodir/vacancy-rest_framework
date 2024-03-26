from django.urls import path
from .views import *
urlpatterns = [
    path('',VacancyListApi.as_view()),
    path('create/category/',CategoryCreateApi.as_view()),
    path('create/company/',CompanyCreateApi.as_view()),
    path('create/vacancy/',VacancyCreateApi.as_view()),
    path('create/application/',ApplicationsCreateApi.as_view()),
    path('list/application/',ApplicationsListApi.as_view()),
    path('more_info/<int:pk>/',VacancyRetrieveApi.as_view())
]
 
