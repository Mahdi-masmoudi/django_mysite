from django.contrib import admin
from .models import Produit
from .models import categorie
from .models import fournisseur
from .models import ProduitNC
from .models import Commande
admin.site.register(Commande)
admin.site.register(ProduitNC)
admin.site.register(fournisseur)
admin.site.register(categorie)
admin.site.register(Produit)

# Register your models here.
