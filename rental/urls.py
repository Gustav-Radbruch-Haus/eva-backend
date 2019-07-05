from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='rentalDashboardIndex'),
    path('dashboard/', views.index, name='rentalDashboard'),
    path('request/', views.makeRequest, name='makeRequest'),
    path('request/<slug:requestSlug>/', views.showDetails, name='requestDetail'),
    path('request/<slug:requestSlug>/accept', views.acceptRequest, name='acceptRequest'),
]