from django.urls import path
from . import views
from .models import Product
from django.views.generic import ListView, DetailView
urlpatterns = [
    path('', ListView.as_view(
        queryset = Product.objects.all().order_by('date'),
        template_name = 'product/productlist.html',
        context_object_name = 'Products',
        paginate_by = 1) , name= 'product'),
    path('<int:pk>', views.post , name= 'post'),
]