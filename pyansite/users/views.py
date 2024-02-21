from django.shortcuts import render
from .forms import RegistrationForm
from django.contrib.auth.models import User


def register(request):

    if request.method == 'POST':

        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            user = User.objects.create_user(data.name, data.email, data.password)
            user.save()
            return render(request, 'users/register_done.html')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})
