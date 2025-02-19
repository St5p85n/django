from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from  django.contrib.auth.hashers import make_password

from .models import Utilisateur
# Create your views here.
def addUtilisateur(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = make_password(request.POST.get('password'))
        email = request.POST.get('email')
        biographie = request.POST.get('biographie')
        competence = request.POST.get('competence')
        u= Utilisateur.objects.create(username=username,password=password,email=email,biographie=biographie,competence=competence)
        u.save()
        login(request,u)
        return redirect('liste')

    return render(request,'user/add.html')
def deconnexion(request):
    logout(request)
    return redirect('liste')
def connexion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('liste')

    return render(request,'user/login.html')
