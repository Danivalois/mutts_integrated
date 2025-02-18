from django.shortcuts import render


def home(request):
    return render(request, "home.html")  # ✅ Use only "home.html", Django will find it

def about(request):
    return render(request, "about.html")  # ✅ Use only "about.html"

def products(request):
    return render(request, 'products/products.html') 

