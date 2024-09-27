from django.shortcuts import render, redirect,get_object_or_404
from django.http import JsonResponse
from .models import PurchaseMaster, PurchaseDetails, Supplier, Item

def purchase_list(request):
    purchases = PurchaseMaster.objects.filter(status=1).order_by('-datetime')
    return render(request, 'purchase_list.html' , {'purchases' : purchases })


def purchase_master(request):
    if request.method == "POST":
        # Extract form data
        invoice_no = request.POST.get('invoice_no')
        invoice_date = request.POST.get('invoice_date')
        supplier_id = request.POST.get('supplier_id')
        total_amount = 0  # Initialize total amount

        # Create the PurchaseMaster object
        supplier = Supplier.objects.get(id=supplier_id)
        purchase_master = PurchaseMaster.objects.create(
            invoice_no=invoice_no,
            invoice_date=invoice_date,
            supplier_id=supplier,
            total_amount=0  # This will be updated after PurchaseDetails are added
        )

        # Process the items[] data sent as hidden inputs
        items = request.POST.getlist('items[]')  # Fetch all items[] sent via POST

        # Loop through the items and create PurchaseDetails
        for item in items:
            item_data = item.split(',')  # Format: "item_id,quantity,total"
            item_id = item_data[0]
            quantity = int(item_data[1])
            total = float(item_data[2])

            # Fetch item and price
            item_obj = Item.objects.get(id=item_id)
            price = item_obj.unit_price  # Assuming 'unit_price' is a field in your 'Item' model

            # Create PurchaseDetails record
            PurchaseDetails.objects.create(
                item_id=item_obj,
                quantity=quantity,
                price=price,
                amount=total,
                purchase_master_id=purchase_master  # Using purchase_master_id
            )

            # Update total_amount for PurchaseMaster
            total_amount += total

        # After all PurchaseDetails are added, update the total amount in PurchaseMaster
        purchase_master.total_amount = total_amount
        purchase_master.save()

        # Redirect or render success page
        return redirect('purchase_list')  # You can replace 'success_page' with your desired route

    # Render the form (GET request)
    suppliers = Supplier.objects.filter(status=1)
    items = Item.objects.filter(status=1)
    return render(request, 'purchase_master.html', {'suppliers': suppliers, 'items': items})


# Function to fetch item rate via AJAX
def get_item_rate(request):
    item_id = request.GET.get('item_name_id')
    try:
        item = Item.objects.get(id=item_id)
        return JsonResponse({'rate': item.unit_price})
    except Item.DoesNotExist:
        return JsonResponse({'rate': 0})
    

def purchase_view(request, purchase_id):
    # Get the purchase by ID
    purchase = get_object_or_404(PurchaseMaster, id=purchase_id)

    # Fetch all related purchase details
    purchase_details = PurchaseDetails.objects.filter(purchase_master_id=purchase)

    return render(request, 'purchase_view.html', {
        'purchase': purchase,
        'purchase_details': purchase_details,
    })
  

