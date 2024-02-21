from django.shortcuts import render
from .models import TeamDatabase, ProjectDatabase


def team_data(request):
    team = TeamDatabase.objects.all()
    return render(request, 'main/team.html', {'team': team})


def projects_data(request):
    projects = ProjectDatabase.objects.all()
    return render(request, 'main/projects.html', {'projects': projects})
