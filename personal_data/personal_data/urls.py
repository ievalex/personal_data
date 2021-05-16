from django.conf.urls import url, include
from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework import routers, serializers, viewsets
from app import forms, views, models, serializers

#----------------------Код для API--------

# конфигурируем адрес для заявителей
router = routers.DefaultRouter()
router.register(r'api/requesters', views.RequesterViewSet)

# конфигурируем адрес для кандидатов
router.register(r'api/candidates', views.CandidateViewSet)

# конфигурируем адрес для индивидуальных предпринимателей
router.register(r'api/individuals', views.IndividualBusinessmanViewSet)

#-----------------------------------------

urlpatterns = [
    path('', views.home, name='home'),
    url(r'^', include(router.urls)),
    path('requesters/', views.requesters, name='requesters'),
    path('candidates/', views.candidates, name='candidates'),
    path('individuals/', views.individuals, name='individuals'),
    path('requesters/item_create/', views.requester_create, name='requester_create'),
    path('requesters/item_edit/<int:id>/', views.requester_edit),
    path('requesters/item_delete/<int:id>/', views.requester_delete),
    path('candidates/item_create/', views.candidate_create, name='candidate_create'),
    path('candidates/item_edit/<int:id>/', views.candidate_edit),
    path('candidates/item_delete/<int:id>/', views.candidate_delete),  
    path('individuals/item_create/', views.individual_create, name='individual_create'),
    path('individuals/item_edit/<int:id>/', views.individual_edit),
    path('individuals/item_delete/<int:id>/', views.individual_delete),  
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
