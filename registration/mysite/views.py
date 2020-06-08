
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def index(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Cette email a déja un compte")
                return redirect('index')

            elif len(password) < 8:
                messages.info(request, 'Le mot de passe est inférieur à 8 caractères')
                return redirect('login')
                
            else:
                add = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email,
                                                password=password)
                add.save()
                print('Votre profile a été créé')
                return redirect('login')

        else:
            messages.info(request, 'Mot de passe non confirmé')
            return redirect('index')

    else:
        return render(request, 'index.html')


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        add = auth.authenticate(request, username=username, password=password)

        if add is not None:
            auth.login(request, add)
            return redirect('home')
        else:
            messages.info(request, 'Identifiant invalide')
            return redirect('login')

    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')


def password_reset(request):
    return render(request, 'password_reset.html')
