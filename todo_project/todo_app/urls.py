
from django.urls import path
from . import views
from .models import task

urlpatterns = [
  path('',views.TaskListView.as_view(),name='home'),
  path('delete/<int:id>',views.Delete,name='delete'),
  path('create',views.Create,name='create' ),
  path('update/<int:pk>',views.TaskUpdateView.as_view(),name='update')
]