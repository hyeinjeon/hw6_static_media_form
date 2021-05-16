from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('main2/', main2, name="main2"),
    path('detail2/<str:id>', detail2, name="detail2"),
    path('new2/', new2, name="new2"),
  #  path('create2/', create2, name="create2"),
    path('edit2/<str:id>', edit2, name="edit2"),
  #  path('update2/<str:id>', update2, name="update2"),
    path('delete2/<str:id>', delete2, name="delete2"),
] 
