# shop/views.py
from django.views.generic import TemplateView, ListView
from .models import Product
from .models import Category
import random

class CategoryProductsView(ListView):
    model = Product
    template_name = 'category_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return Product.objects.filter(category__id=category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        context['category'] = Category.objects.get(id=category_id)
        return context


class HomePageView(ListView):
    template_name = 'home.html'
    model = Product
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        # Statik mahsulotlar o'rniga ma'lumotlar bazasidan olish
        context = super().get_context_data(**kwargs)
        
        # Product modelidan 8 ta tasodifiy mahsulotni olish
        products = Product.objects.all()
        context['products'] = random.sample(list(products), 8)  # 8 tasini tasodifiy tanlash
        return context



class CategoryView(TemplateView):
    template_name = 'category.html'

class SingleProductView(TemplateView):
    template_name = 'single_product.html'  

class CheckoutView(TemplateView):
    template_name = 'checkout.html'  

class CartView(TemplateView):
    template_name = 'cart.html'  

class ConfirmationView(TemplateView):
    template_name = 'confirmation.html'  

class SingleProductView(TemplateView):
    template_name = 'single-product.html'

class ContactView(TemplateView):
    template_name = 'contact.html'  

class CategoryListView(ListView):
    model = Category
    template_name = '/components/category.html'  
    context_object_name = 'categories'  
    print(model)