from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contacts', views.info, name='contacts'),
    path('old_projects', views.projects, name='old_projects'),
    path('old_team', views.team, name='old_team'),
    path('music', views.music, name='music'),
    path('work', views.work, name='work'),
]
