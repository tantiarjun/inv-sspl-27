from django.urls import path
from . import views

urlpatterns = [
    path('purchase/', views.purchase_list, name='purchase_list'),
    path('purchase-master/', views.purchase_master, name='purchase_master'),
    path('get-item-rate/', views.get_item_rate, name='get_item_rate'),
    path('purchase/<int:purchase_id>/', views.purchase_view, name='purchase_view'),
    
]
