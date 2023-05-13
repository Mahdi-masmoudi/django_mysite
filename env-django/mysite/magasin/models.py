from distutils.command.upload import upload
from django.db import models
from datetime import date


class categorie(models.Model):
    TYPE_CHOICES = [
        ('Al', 'Alimentaire'),
        ('Mb', 'Meuble'),
        ('Sn', 'Sanitaire'),
        ('Vs', 'Vaisselle'),
        ('Vt', 'Vêtement'),
        ('Jx', 'Jouets'),
        ('Lg', 'Linge de Maison'),
        ('Bj', 'Bijoux'),
        ('Dc', 'Décor')
    ]
    name = models.CharField(default='Al', choices=TYPE_CHOICES, max_length=50)

    def __str__(self):
        return self.name


class Produit(models.Model):
    TYPE_CHOICES = [('em', 'emballé'), ('fr', 'Frais'), ('cs', 'Conserve')]
    libelle = models.CharField(max_length=100)
    description = models.TextField(default='non definie')
    prix = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default='em')
    image = models.ImageField(blank=True, upload_to='media/')
    categorie = models.ForeignKey(
        'categorie', on_delete=models.CASCADE, null=True)
    fournisseur = models.ForeignKey(
        'fournisseur', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "la libelle : "+self.libelle+"la description : "+self.description + "le prix  : "+str(self.prix)+"le type : "+self.type+"image : "+str(self.image)


class fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.TextField(default=" ")
    email = models.EmailField(default=" ")
    telephone = models.CharField(max_length=8)

    def __str__(self):
        return self.nom+" "+self.adresse+" "+self.telephone


class ProduitNC(Produit):
    Duree_garantie = models.CharField(max_length=100)

    def __str__(self):
        return "libelle : "+self.libelle+" Prix : "+str(self.prix) + "Garantie : "+self.Duree_garantie


class Commande(models.Model):
    dateCde = models.DateField(null=True, default=date.today)
    totalCde = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    produits = models.ManyToManyField(Produit)
    fournisseurs = models.ManyToManyField(fournisseur)

    def __str__(self):
        return str(self.dateCde)
