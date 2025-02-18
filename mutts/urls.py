from django.contrib import admin
from django.urls import path, include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, about
from . import views
from products.views import products  # Adicione esta linha para importar a view 'products'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('products/', products, name='products'),  # Certifique-se de que essa linha está correta
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)








