from django.shortcuts import render
from accounts.forms import LoginForm
from django.contrib.auth import authenticate, login


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})
