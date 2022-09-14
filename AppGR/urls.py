from django.urls import path

from AppGR import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('sombras/', views.sombras, name="sombras"),
    path('base/', views.base, name="base"),
    path('brochas/', views.brochas, name="brochas"),
    path('sombras_formulario/', views.sombras_formulario, name="sombras_formulario"),
    path('form_busqueda_sombras/', views.busqueda_sombras, name="form_busqueda_sombras"),
    path('busqueda_sombras/', views.buscar_sombras, name="busqueda_sombras"),
    path('base_formulario/', views.base_formulario, name="base_formulario"),
    path('form_busqueda_base/', views.busqueda_base, name="form_busqueda_base"),
    path('busqueda_base/', views.buscar_base, name="busqueda_base"),
    path('brochas_formulario/', views.brochas_formulario, name="brochas_formulario"),
    path('form_busqueda_brochas/', views.busqueda_brochas, name="form_busqueda_brochas"),
    path('busqueda_brochas/', views.buscar_brochas, name="busqueda_brochas"),

]