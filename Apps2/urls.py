from django.urls import path,include
from . import views

urlpatterns = [
  path('', views.getData),
  path('create', views.addUser),
  path('list/<str:pk>', views.getUser),
  path('update/<str:id>', views.updateUser),
  path('delete/<str:id>', views.deleteUser),
  
]
