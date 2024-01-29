from django.urls import path
from . import views

app_name = 'TodoList'

urlpatterns = [
    path('',views.index, name = 'index'),
    path('delete/<int:list_id>',views.delete,name='delete'),
    path('checked/<int:list_id>',views.completed,name='completed')
]