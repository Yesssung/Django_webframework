from django.urls import path
from projectapp import views

urlpatterns = [
    path('',views.index),
    path('create/',views.create),
    path('read/<id>/',views.read),
    path('delete/', views.delete),
    path('update/<id>/',views.update)
]
