from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.permissions import IsAuthenticated

from shop.models import Categorie, Produit
from rest_framework import generics
from .serializers import CategorieSerializer
from django.contrib.auth.models import Permission,Group
# Create your views here.

class AjoutListeCategorieView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
class ModificationSupressionCategorieView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

@login_required
def listeCategorie(request):
    liste = Categorie.objects.all()
    return render(request, 'categorie/liste.html', context={'categories':liste})

def addCategorie(request):
    if request.method == "POST":
        lib = request.POST.get("libelle")
        Categorie.objects.create(libelle=lib)
        return redirect('liste')
    return  render(request, 'categorie/add.html')
def deleteCategorie(request,idC):
    Categorie.objects.filter(id=idC).delete()
    return redirect('liste')

def editCategorie(request,idC):
    #categorie = Categorie.objects.filter(id=idC)
    if request.method=="POST":
        lib = request.POST.get("libelle")
        idc = request.POST.get('id')
        Categorie.objects.filter(id=idc).update(libelle=lib)
        return redirect('liste')
    categorie = get_object_or_404(Categorie,id=idC)
    return  render(request, 'categorie/edit.html', context={"categorie":categorie})

def listProduit(request):
    produits = Produit.objects.all()
    paginer = Paginator(produits,2)
    numeroDePage = request.GET.get('numberoPage')
    prduitPage = paginer.get_page(numeroDePage)
    return render(request,'produit/liste.html',context={'produits':prduitPage})
def addProduit(request):
    if request.method=='POST':
        nom = request.POST.get('nom')
        description = request.POST.get('description')
        prix = request.POST.get('prix')
        photo = request.FILES['nomPhoto']
        cate = request.POST.get('idCategorie')
        categorie = get_object_or_404(Categorie,id=cate)
        Produit.objects.create(nom=nom,description=description,prix=prix,photoPro=photo,categorie=categorie)
        return  redirect('listeP')
    categories = Categorie.objects.all()
    return render(request,'produit/add.html',context={'categories':categories})

def verifGroup(request):
   groupe,created= Group.objects.get_or_create(name='adminclasse')
   if created:
       print('Le groupe vient d etre cree')
   else:
       # request.user.user_permissions.add(permission)
       request.user.groups.remove(groupe)
       print('le group existait deja')

   return redirect('listeP')