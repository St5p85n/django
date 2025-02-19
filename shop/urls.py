
from  django.urls import path
from .views import listeCategorie,addCategorie,deleteCategorie,editCategorie,listProduit,addProduit,verifGroup
from .views import AjoutListeCategorieView,ModificationSupressionCategorieView

urlpatterns =[
    path('categorie/', listeCategorie, name='liste'),
    path('categorie/ajouter/', addCategorie, name='add'),
    path('categorie/supprimer/<int:idC>', deleteCategorie, name='sup'),
    path('categorie/modifier/<int:idC>', editCategorie, name='edit'),
    path('produit/', listProduit, name='listeP'),
    path('produit/ajouter/', addProduit, name='addP'),
    path('api/categorie/',AjoutListeCategorieView.as_view(),name='api_categorie'),
    path('api/categorie/<int:pk>', ModificationSupressionCategorieView.as_view(), name='api_categorie_id'),
    #path('produit/supprimer/<int:idC>', deleteCategorie, name='supP'),
    #path('produit/modifier/<int:idC>', editCategorie, name='editP'),
    path('verifGroup/',verifGroup,name='verifG')
]