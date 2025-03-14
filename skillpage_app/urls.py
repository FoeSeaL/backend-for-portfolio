from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project/', views.ProjectView.as_view(), name='project'),
    path('contact/', views.ContactView.as_view(), name='contact'),


    path('about/', views.AboutView.as_view(), name='about'),

    path('skills/', views.SkillsListView.as_view(), name='skills'),

    path('skills/new/', views.SkillCreateView.as_view(), name='skill-create'),
    path('skills/<int:pk>/update/', views.SkillUpdateView.as_view(), name='skill-update'),
    path('skills/<int:pk>/delete/', views.SkillDeleteView.as_view(), name='skill-delete'),
    path('categories/new/', views.CategoryCreateView.as_view(), name='category-create'),
]