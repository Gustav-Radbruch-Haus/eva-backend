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
]