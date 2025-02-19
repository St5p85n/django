from django.db import models

# Create your models here.
class Categorie(models.Model):
    libelle = models.CharField(max_length=100)
    def __str__(self):
        return self.libelle
class Produit(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE,related_name='produits')
    photoPro = models.ImageField(upload_to='image/', blank=True)
    def __str__(self):
        return f"{self.nom} - {self.description}"