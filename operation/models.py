from django.db import models
from django.utils import timezone
from master.models import Supplier, Item


# Purchase Master Model
class PurchaseMaster(models.Model):
    invoice_no = models.CharField(max_length=100, blank=True, null=True)
    invoice_date = models.DateField(blank=True, null=True)
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    total_amount = models.FloatField(blank=True, null=True)
    datetime = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.invoice_no

# Purchase Details Model
class PurchaseDetails(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    datetime = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=True)
    purchase_master_id = models.ForeignKey(PurchaseMaster, on_delete=models.CASCADE)  # Foreign key corrected

    def __str__(self):
        return f"{self.item_id} - {self.purchase_master_id}"
