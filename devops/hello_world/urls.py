from django.urls import path

from . import views

urlpatterns = [
    path('/test', views.test.as_view()),
    path('/hello', views.hello.as_view())
]
 
 
 