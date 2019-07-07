from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.index, name='redirect-to-login'),
    path('', views.index, name='rentalDashboardIndex'),
    path('dashboard/', views.index, name='rentalDashboard'),
    path('request/', views.makeRequest, name='makeRequest'),
    path('request/<slug:requestSlug>/', views.showDetails, name='requestDetail'),
    path('request/<slug:requestSlug>/accept', views.acceptRequest, name='acceptRequest'),
    path('request/<slug:requestSlug>/reject', views.rejectRequest, name='rejectRequest'),
    path('request/<slug:requestSlug>/start', views.startRequest, name='startRequest'),
    path('request/<slug:requestSlug>/finish', views.finishRequest, name='finishRequest'),
    path('request/<slug:requestSlug>/clarify', views.clarifyRequest, name='clarifyRequest'),
]