from task import views
from django.urls import path

urlpatterns = [
    path('', views.taskViwer, name='taskViwer')
]