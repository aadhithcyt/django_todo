from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_todo, name='add'),
    path('view/<int:id>/', views.view_todo, name='view'),
    path('edit/<int:id>/', views.edit_todo, name='edit'),
    path('delete/<int:id>/', views.delete_todo, name='delete'),
]
