from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User


def index(request):
    user = User
    return render(request, 'main/index.html', {'user': user})


def info(request):
    return render(request, 'main/contacts.html')


def projects(request):
    return render(request, 'main/projects.html')


def team(request):
    return render(request, 'main/team.html')


def music(request):
    return render(request, 'main/music.html')


def work(request):
    return render(request, 'main/work.html')


@login_required
def profile(request):
    return render(request, 'main/profile.html')
