from django.urls import path
from . import views

urlpatterns = [

    # path('' , views.item_list , name='item_list'),
    # path('add_item/',views.add_item , name='add_item'),
    # path('edit_item/<int:item_id>/',views.edit_item , name='edit_item'),
    # path('delete_item/<int:item_id>/',views.delete_item , name='delete_item'),
    
    path('' , views.item_action , name='item_action'),
    path('items/<str:action>/', views.item_action, name='item_action'),
    path('items/<str:action>/<int:item_id>/', views.item_action, name='item_action_with_id'),
    
    path('supplier/', views.supplier_list, name='supplier_list'),
    path('add_supplier/',views.add_supplier , name='add_supplier'),
    path('edit_supplier/<int:supplier_id>/',views.edit_supplier , name='edit_supplier'),
    path('delete_supplier/<int:supplier_id>/',views.delete_supplier , name='delete_supplier'),
]





