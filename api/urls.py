from django.urls import path
from . import views

urlpatterns = [
    path('', views.stu_form,name='stu_insert'), 
    path('<int:id>/', views.stu_form,name='stu_update'), 
    path('delete/<int:id>/',views.stu_delete,name='stu_delete'),
    path('list/',views.list,name='list') 
]
