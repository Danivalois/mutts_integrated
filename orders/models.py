from django.db import models
import uuid
from django.apps import apps  # ✅ Import Django's app resolver
from django.core.exceptions import ValidationError


class Order(models.Model):
    customer = models.ForeignKey("customers.Customer", on_delete=models.CASCADE)  # ✅ Use string reference
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)  # ✅ Use string reference
    order_ID = models.CharField(max_length=50, unique=True)
    order_payment_ID = models.CharField(max_length=50, unique=True)
    order_status = models.CharField(max_length=20)
    order_quantity = models.IntegerField()
    order_freight_cost = models.DecimalField(max_digits=10, decimal_places=2)
    order_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order_ID}"
        
    order_freight_service = models.CharField(
        max_length=50, choices=[("PAC", "PAC"), ("SEDEX", "SEDEX"), ("PACMINI", "PACMINI"), ("JADLOG", "JADLOG")]
    )

    order_zip_code = models.CharField(max_length=8)
    order_street = models.CharField(max_length=255)
    order_neighborhood = models.CharField(max_length=255)
    order_city = models.CharField(max_length=255)
    order_state = models.CharField(max_length=2)
    order_house_number = models.CharField(max_length=20)
    order_complement = models.CharField(max_length=255, blank=True, null=True)
    order_phone = models.CharField(max_length=20, blank=True, null=True)
    order_email = models.EmailField(blank=True, null=True)
    order_created_at = models.DateTimeField(auto_now_add=True)
    order_updated_at = models.DateTimeField(auto_now=True)
    order_is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Order {self.order_ID} - {self.order_status}"
