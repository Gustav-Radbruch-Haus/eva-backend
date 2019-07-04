from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/', views.index, name='rentalDashboard'),
    path('request/', views.makeRequest, name='makeRequest'),
    path('request/<slug:requestSlug>/', views.showDetails, name='requestDetail'),
]