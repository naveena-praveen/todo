
from django.urls import path
from . import views
from .models import task

urlpatterns = [
  path('',views.home,name='home'),
  path('delete/<int:id>',views.delete,name='delete'),
  path('create',views.create,name='create' ),
  path('update/<int:id>',views.update,name='update')
]