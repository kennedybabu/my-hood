from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.home, name='home'),
    path('hood/<int:pk>/', views.hood, name='hood'), 
    path('create_hood/', views.createHood, name='create_hood'),
    path('update_hood/<int:pk>/', views.updateHood, name='update_hood'),
    path('delete_hood/<int:pk>/', views.deleteHood, name='delete_hood')
]