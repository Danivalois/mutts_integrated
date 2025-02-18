from django.db import models
import os
from django.core.exceptions import ValidationError

def validate_jpg(value):
    """Ensure the product image is a .jpg file."""
    ext = os.path.splitext(value.name)[1]
    if ext.lower() != ".jpg":
        raise ValidationError("Only .jpg files are allowed for product images.")

#class Category(models.Model):
 #   name = models.CharField(max_length=100, unique=True)

  #  def __str__(self):
   #     return self.name











from django.core.validators import MinValueValidator

class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_code = models.CharField(max_length=50, unique=True)
    product_short_description = models.CharField(max_length=255, blank=True, null=True)
    product_description_long = models.TextField(blank=True, null=True)
    product_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    product_unit_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    product_stock = models.IntegerField(default=0)
    product_thumbnail_url = models.CharField(max_length=500, blank=True, null=True)
    product_brand = models.CharField(max_length=100, blank=True, null=True)
    product_sku = models.CharField(max_length=100, unique=True)
    product_dimensions = models.CharField(max_length=255, blank=True, null=True)  # Displayed dimension
    product_weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    product_height = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    product_width = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    product_length = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    product_image_url = models.ImageField(upload_to="product_images/")  
    product_created_at = models.DateTimeField(auto_now_add=True)
    product_updated_at = models.DateTimeField(auto_now=True)
    product_is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.product_description_short


