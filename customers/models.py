from django.db import models
import re
from django.core.validators import RegexValidator, EmailValidator, ValidationError
from localflavor.br.models import BRCPFField

def validate_cpf(value):
    """Ensure CPF has exactly 11 digits."""
    if not re.match(r'^\d{11}$', value):
        raise ValidationError("CPF must contain exactly 11 digits.")




class Customer(models.Model):
    customer_cpf = BRCPFField(unique=True, verbose_name="CPF")  # Validates CPF format
    customer_name = models.CharField(max_length=100, blank=False)
    
    customer_zip_code = models.CharField(max_length=9, validators=[RegexValidator(r'^\d{5}-\d{3}$')], verbose_name="CEP")
    customer_street = models.CharField(max_length=255, blank=False)
    customer_neighborhood = models.CharField(max_length=100, blank=False)
    customer_city = models.CharField(max_length=100, blank=False)
    customer_state = models.CharField(max_length=2, blank=False)  # Ex: SP, RJ
    customer_house_number = models.CharField(max_length=10, blank=False)
    customer_complement = models.CharField(max_length=100, blank=True, null=True)
    
    customer_phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Telefone")
    customer_email = models.EmailField(blank=True, null=True, validators=[EmailValidator()])

    customer_created_at = models.DateTimeField(auto_now_add=True)
    customer_updated_at = models.DateTimeField(auto_now=True)
    customer_is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.customer_name} ({self.customer_cpf})"










class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="addresses")
    zip_code = models.CharField(max_length=8)
    street = models.CharField(max_length=255)
    neighborhood = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    house_number = models.CharField(max_length=20)
    complement = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.street}, {self.house_number} - {self.city}/{self.state}"
    

    
