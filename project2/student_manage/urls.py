
from django.urls import path
from .import views

urlpatterns = [
    path('', views.student_list, name='home'),
    path('update/<int:id>/', views.update_student, name='update'),
    path('delete/<int:id>/', views.delete_student, name='delete'),
    path('add_student/', views.add_student, name='add'),
    path('search/', views.search, name='search'),
]
