from django.urls import path

from AppGR import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('sombras/', views.sombras, name="sombras"),
    path('base/', views.base, name="base"),
    path('brochas/', views.brochas, name="brochas"),
    path('crear-sombras/', views.sombras_formulario, name="sombras_formulario"),
    path('busqueda-sombras-form/', views.busqueda_sombras, name="busqueda_sombras_form"),
    path('busqueda-sombras/', views.buscar_sombras, name="busqueda_sombras"),
    path('crear-base/', views.base_formulario, name="base_formulario"),
    path('busqueda-base-form/', views.busqueda_base, name="busqueda_base_form"),
    path('busqueda-base/', views.buscar_base, name="busqueda_base"),
    path('crear-brochas/', views.brochas_formulario, name="brochas_formulario"),
    path('busqueda-brochas-form/', views.busqueda_brochas, name="busqueda_brochas_form"),
    path('busqueda-brochas/', views.buscar_brochas, name="busqueda_brochas"),

]