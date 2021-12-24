from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hood/<int:pk>/', views.hood, name='hood')
]