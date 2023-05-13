from django.shortcuts import loader, redirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Commande, Produit
from .forms import CommandeForm, ProduitForm
from .models import Produit
from .models import fournisseur
from .forms import ProduitForm, FournisseurForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


@login_required
def listProd(request):
    list = Produit.objects.all()
    return render(request, 'magasin/vitrine.html', {'list': list})


@login_required
def Mesfourniseur(request):
    list = fournisseur.objects.all()
    return render(request, 'magasin/mesFournisseur.html', {'list': list})

##########################################################################################
@login_required
def listCommande(request):
    list = Commande.objects.all()
    return render(request, 'magasin/affichercommande.html', {'list': list})

def addfourni(request):
    if request.method == "POST":
        form = FournisseurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FournisseurForm()
    produits = fournisseur.objects.all()
    return render(request, 'magasin/testForm.html', {'produits': produits, 'form': form})


def fourni_det(request, id):
    f = get_object_or_404(fournisseur, id=id)
    return render(request, 'magasin/viewfourni.html', {'fournisseur': f})


def edit_four(request, id):
    p = fournisseur.objects.get(id=id)
    form = FournisseurForm(instance=p)

    if request.method == 'POST':
        form = FournisseurForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
            return redirect('four')

    return render(request, 'magasin/updatefour.html', {'form': form, 'fournisseur': p})


def deletefou(request, id):
    post = get_object_or_404(fournisseur, pk=id)
    context = {'post': post}

    if request.method == 'GET':
        return render(request, 'magasin/deletefounisseur.html', context)
    elif request.method == 'POST':
        post.delete()
        messages.success(request,  'The post has been deleted successfully.')
        return redirect('four')

################################################################################################################


def index(request):
    return render(request, 'magasin/base.html')

################################################################################################################


def editProd(request):
    if request.method == "POST":
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Produit')
    else:
        form = ProduitForm()
    produits = Produit.objects.all()
    return render(request, 'magasin/majProduits.html', {'produits': produits, 'form': form})


def edit_product(request, product_id):
    p = Produit.objects.get(id=product_id)
    form = ProduitForm(instance=p)

    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
            return redirect('Produit')

    return render(request, 'magasin/updateProd.html', {'form': form, 'produit': p})


def product_det(request, product_id):
    p = get_object_or_404(Produit, id=product_id)
    return render(request, 'magasin/viewProd.html', {'product': p})


def deleteProd(request, id):
    post = get_object_or_404(Produit, pk=id)
    context = {'post': post}

    if request.method == 'GET':
        return render(request, 'magasin/delete.html', context)
    elif request.method == 'POST':
        post.delete()
        messages.success(request,  'The post has been deleted successfully.')
        return redirect('Produit')
##############################################################################################


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(
                request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def add_commande(request):
    # Create an empty form for adding a new commande
    form = CommandeForm()

    if request.method == 'POST':
        # Fill the form with the submitted data
        form = CommandeForm(request.POST)

        if form.is_valid():
            # Save the commande instance to the database
            commande = form.save()

            # Add the selected products to the commande instance
            for produit_id in request.POST.getlist('produits'):
                produit = Produit.objects.get(id=produit_id)
                commande.produits.add(produit)

            # Update the totalCde field based on the selected products' prices
            total = sum([produit.prix for produit in commande.produits.all()])
            commande.totalCde = total
            commande.save()

            # Redirect to the detail view of the newly created commande
            return redirect('detailcomm', commande.pk)

    context = {
        'form': form,
        'produits': Produit.objects.all(),
    }

    return render(request, 'magasin/commande/cart.html', context)

def commande_detail(request,id):
    commande = get_object_or_404(Commande, pk=id)
    context = {
        'commande': commande
    }
    return render(request, 'magasin/commande/commande_detail.html', context)

