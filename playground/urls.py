from django.urls import path
from . import views

urlpatterns = [
    path('exports/', views.export_dashboard, name='export_dashboard'),
    path('keys/export/', views.export_keys_excel, name='export_keys_excel'),
    path('misc/export/', views.export_miscitem_excel, name='export_miscitem_excel'),
    path('fixedassets/export/', views.export_fixedassets_excel, name='export_fixedassets_excel'),
    path('ppes/export/', views.export_ppes_excel, name='export_ppes_excel'),
    path('spareitems/export/', views.export_spareitems_excel, name='export_spareitems_excel'),
    path('teaitems/export/', views.export_teaitems_excel, name='export_teaitems_excel'),
    path('consumables/export/', views.export_consumables_excel, name='export_consumables_excel'),
    path('stationary/export/', views.export_stationary_excel, name='export_stationary_excel'),
]
