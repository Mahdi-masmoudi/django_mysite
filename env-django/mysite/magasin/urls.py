from django.urls import path
from . import views
from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
urlpatterns = [
    path('', views.index, name='index'),
    
    #####################################################################
    
    path('listProduits', views.listProd, name='Produit'),
    path('editProduit', views.editProd, name='edit'),
    path('viewProd/<int:product_id>/view',views.product_det, name='product_det'),
    path('product_det', views.product_det, name='product_det'),
    path('updateProd/<int:product_id>/edit/', views.edit_product, name='edit_product'),
    path('delete/<int:id>/', views.deleteProd, name='deleteProd'),
    
    ###################################################################
    
    path('nouvFourbisseur/', views.addfourni, name='addfourni'),
    path('mesFournisseur', views.Mesfourniseur, name='four'),
    path('deletefounisseur/<int:id>/', views.deletefou, name='deletefourni'),
    path('viewFour/<int:id>/view',views.fourni_det, name='fourni_det'),
    path('fourni_det', views.fourni_det, name='fourni_det'),
    path('updatefour/<int:id>/edit/', views.edit_four, name='edit_four'),
   
    ###################################################################
   path('listcommande/', views.listCommande, name='com'),
   ############################################################""
    path('register/', views.register, name='register'),
   

    ####################password reset ########################
    path('password-reset/', PasswordResetView.as_view(template_name='magasin/password/password_reset.html'),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='magasin/password/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='magasin/password/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='magasin/password/password_reset_complete.html'),name='password_reset_complete'),

#######################################################
   path("add_commande",views.add_commande,name="commande"),
  path('detail_commande/<int:id>/',views.commande_detail,name="detailcomm")
]
