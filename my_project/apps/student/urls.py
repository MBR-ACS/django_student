from django.urls import path
from . import views

urlpatterns = [
    # path('', views.student, name='student'),
    path('studentslist/', views.list_students, name='list_students'),
    path('add/', views.add_student, name='add_student'),
    path('delete/<uuid:id>/', views.delete_student, name='delete_student'),
    path('edit/<uuid:id>/', views.edit_student, name='edit_student'),
]
