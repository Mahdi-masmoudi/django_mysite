from django import forms
from .models import Commande, Produit
from .models import fournisseur
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm


class FournisseurForm(ModelForm):
    class Meta:
        model = fournisseur
        fields = "__all__"


class CommandeForm(forms.ModelForm):
    produits = forms.ModelMultipleChoiceField(
        queryset=Produit.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    fournisseurs = forms.ModelMultipleChoiceField(
        queryset=fournisseur.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Commande
        exclude = ['totalCde']

class ProduitForm(ModelForm):
    class Meta:
        model = Produit
        fields = "__all__"


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + \
            ('first_name', 'last_name', 'email')
