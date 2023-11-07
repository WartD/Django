from django.shortcuts import render
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from login.forms import LoginForm, RegisterForm


# Create your views here.

def loginPage(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'],
                                password = form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Неверные данные')

    return render(request, "login.html", {'form': form})

def registerPage(request):
    form = RegisterForm()

    if request.method == 'POST':
        # заполняем объект данными формы, если она была отправлена
        form = RegisterForm(request.POST)

        if form.is_valid():
            # если форма валидна - создаем нового пользователя
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            return redirect('login')
    # ренедерим шаблон и передаем объект формы
    return render(request, 'registration.html', {'form': form})


def me(request):
    if not request.user.is_authenticated:
        return redirect('home')
        # рендерим шаблон и передаем туда объект пользователя
    return render(request, 'me.html', {'user': request.user})


def doLogout(request):
    logout(request)
    return redirect('login')

# Create your views here.
