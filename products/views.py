# products/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
from django.views.generic import ListView



def home(request):
    return render(request, "home.html")

def products(request):
    return render(request, 'products/products.html')  # Certifique-se do caminho correto


def product_list(request):
    print("🟢 Loading Product List Page")  # Debug log
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, pk):
    print(f"🟢 Loading Product Detail for ID: {pk}")  # Debug log
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

def product_create(request):
    print("🟢 Accessing Product Create Page")  # Debug log
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("✅ Product Created Successfully")
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form})

def product_update(request, pk):
    print(f"🟢 Accessing Update Page for Product ID: {pk}")  # Debug log
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            print("✅ Product Updated Successfully")
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form})

def product_delete(request, pk):
    print(f"🟢 Accessing Delete Page for Product ID: {pk}")  # Debug log
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        print("✅ Product Deleted Successfully")
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})


class ProductListView(ListView):
   model = Product
   template_name = "products/product_list.html"
   context_object_name = "products"
    
#   def get_queryset(self):
#    return Product.objects.values("product_code", "product_short_description")




