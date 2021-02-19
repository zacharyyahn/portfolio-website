from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='homeview'),
    path('projects/', views.ProjectView.as_view(), name='projects'), 
    path('about/', views.AboutView.as_view(), name='about'),
    path('skills/', views.SkillsView.as_view(), name='skills'),
    path('shouldryansitstill/', views.Yes.as_view(), name='skills'),
]