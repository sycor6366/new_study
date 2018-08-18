from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.user_login, name='user_login'),
    path('project/',views.ProjectListView.as_view(), name='project_list'),
    path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project_detail'),
    path('project/<int:pk>/edit', views.project_edit, name='project_edit'),
    path('project/create', views.project_create, name='project_create')
]