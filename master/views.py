from django.shortcuts import render, redirect,get_object_or_404
from .models import Item
from .models import Supplier
from .forms import ItemForm
from .forms import SupplierForm
from django.contrib import messages  # For flash 



# # View to display all items
# def item_list(request):
#     items = Item.objects.filter(status=True).order_by('id')
#     return render(request, 'item/item_list.html', {'items': items})

# View to display all suppliers
def supplier_list(request):
    suppliers = Supplier.objects.filter(status=True).order_by('id')
    return render(request, 'supplier/supplier_list.html', {'suppliers': suppliers})



# # View to add a new item
# def add_item(request):
#     if request.method == "POST":
#         form = ItemForm(request.POST,request.FILES)
#         if form.is_valid():
#             item_name = form.cleaned_data.get('item_name')

#             # Check if an item with the same name already exists
#             if Item.objects.filter(item_name=item_name).exists():
#                 messages.error(request, f"Item '{item_name}' already exists in the database.")
#             else:
#                 form.save()
#                 messages.success(request, f"Item '{item_name}' added successfully!")
#                 return redirect('item_list')  # Redirect to the item list view after saving
#     else:
#         form = ItemForm()

#     return render(request, 'item/add_item.html', {'form': form})

# View to add a new supplier
def add_supplier(request):
    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            supplier_name = form.cleaned_data.get('supplier_name')
            supplier_Phone_No=form.cleaned_data.get('phone_no')
            # Check if an suppiler with the same name already exists
            if Supplier.objects.filter(phone_no=supplier_Phone_No).exists():
                messages.error(request, f"supplier '{supplier_name}' already exists in the database.")
            else:
                form.save()
                messages.success(request, f"supplier '{supplier_name}' added successfully!")
                return redirect('supplier_list')  # Redirect to the supplier list view after saving
    else:
        form = SupplierForm()

    return render(request, 'supplier/add_supplier.html', {'form': form})





# #  View to edit an existing item
# def edit_item(request, item_id):
#     item = get_object_or_404(Item, id=item_id)
#     if request.method == "POST":
#         form = ItemForm(request.POST,request.FILES ,instance=item)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f"supplier '{item}' edited successfully!")
#             return redirect('item_list')
#     else:
#         form = ItemForm(instance=item)
#     return render(request, 'item/edit_item.html', {'form': form, 'item': item})

#  View to edit an existing supplier
def edit_supplier(request, supplier_id):
    supplier = get_object_or_404(Supplier, id=supplier_id)
    if request.method == "POST":
        form = SupplierForm(request.POST,instance=supplier)
        if form.is_valid():
            form.save()
            messages.success(request, f"supplier '{supplier}' edited successfully!")
            return redirect('supplier_list')
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'supplier/edit_supplier.html', {'form': form, 'supplier': supplier})




# #  View to delete an existing item
# def delete_item(request, item_id):
#     item = get_object_or_404(Item, id=item_id)
#     if request.method == "POST":
#         item.status=False
#         item.save()
#         messages.success(request, f"item '{item}' deleted successfully!")
#         return redirect('item_list')
#     return render(request, 'item/delete_item.html', {'item': item})

#  View to delete an existing supplier
def delete_supplier(request, supplier_id):
    supplier = get_object_or_404(Supplier, id=supplier_id)
    if request.method == "POST":
        supplier.status=False
        supplier.save()
        messages.success(request, f"supplier '{supplier}' deleted successfully!")
        return redirect('supplier_list')
    return render(request, 'supplier/delete_supplier.html', {'supplier': supplier})



def item_action(request, action=None, item_id=None):
    """
    Handle different item actions: view, add, edit, delete
    """
    if action == None:
        items = Item.objects.filter(status=True).order_by('id')
        return render(request, 'item/item_action.html', {'items': items})
    
    if action == 'add':
        if request.method == "POST":
            form = ItemForm(request.POST, request.FILES)
            if form.is_valid():
                item_name = form.cleaned_data.get('item_name')
                
                # Check if an item with the same name already exists
                if Item.objects.filter(item_name=item_name).exists():
                    messages.error(request, f"Item '{item_name}' already exists in the database.")
                else:
                    form.save()
                    messages.success(request, f"Item '{item_name}' added successfully!")
                    return redirect('item_action', action='view')  # Redirect to view action after adding
        else:
            form = ItemForm()
        return render(request, 'item/item_action.html', {'form': form, 'action': 'add'})
    
    elif action == 'edit' and item_id:
        item = get_object_or_404(Item, id=item_id)
        if request.method == "POST":
            form = ItemForm(request.POST, request.FILES, instance=item)
            if form.is_valid():
                form.save()
                return redirect('item_action')
        else:
            form = ItemForm(instance=item)
        return render(request, 'item/item_action.html', {'form': form, 'item': item, 'action': 'edit'})
    
    elif action == 'delete' and item_id:
        item = get_object_or_404(Item, id=item_id)
        if request.method == "POST":
            item.status = False
            item.save()
            return redirect('item_action', action='view')
        return render(request, 'item/item_action.html', {'item': item, 'action': 'delete'})
    
    else:
        return redirect('item_action')
