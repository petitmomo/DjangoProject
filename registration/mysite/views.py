
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from .models import Cour 
from django.urls import reverse_lazy
from django.forms import modelformset_factory







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
        return render(request, 'register.html')


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        add = auth.authenticate(request, username=username, password=password)

        if add is not None:
            auth.login(request, add)
            return redirect('cour-index')
        else:
            messages.info(request, 'Identifiant invalide')
            return redirect('login')

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

class CourList(ListView):
    model = Cour
    template_name = 'cour_index.html'
    context_object_name = 'blog_entries'


class CourDetail(DetailView):
    model = Cour
    template_name = 'cour_detail.html'


class CourDelete(DeleteView):
    model = Cour
    template_name = 'cour_delete.html'
    success_url = reverse_lazy('cour-index')
  
class CourCreate(CreateView):
    model = Cour
    template_name = 'cour_create.html'
    fields = ['title', 'slug', 'image', 'content']
    success_url = reverse_lazy('cour-index')

class CourUpdate(UpdateView):
    model = Cour
    template_name = 'cour_edit.html'
    fields = ['title', 'slug', 'image', 'content']
    success_url = reverse_lazy('cour-index')

        

   

