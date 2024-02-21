from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('team', views.team_data, name='team'),
    path('projects', views.projects_data, name='projects')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
