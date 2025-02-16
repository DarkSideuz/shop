# shop/views.py
from django.views.generic import TemplateView, ListView, View, DetailView
import random
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Order, OrderProduct
from django.http import HttpResponse

class CategoryProductsView(ListView):
    model = Product
    template_name = 'category-products.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        category = Category.objects.get(id=category_id)
        return Product.objects.filter(category=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs['category_id']
        category = Category.objects.get(id=category_id)
        context['category'] = category
        return context

class SingleProductView(DetailView):
    model = Product
    template_name = 'single-product.html'
    context_object_name = 'product'

    def get_object(self):
        return Product.objects.get(id=self.kwargs['product_id'])


class AddToCartView(View):
    def post(self, request, *args, **kwargs):
        product_id = self.kwargs.get('pk')
        product = get_object_or_404(Product, id=product_id)
        quantity = request.POST.get('qty', 1)

        # Check if an order exists or create a new one
        order, created = Order.objects.get_or_create(user=request.user, is_completed=False)

        # Add product to the order
        order_product, created = OrderProduct.objects.get_or_create(order=order, product=product)
        order_product.quantity += int(quantity)
        order_product.save()

        return redirect('cart')

class CartView(View):
    def get(self, request, *args, **kwargs):
        order = Order.objects.filter(user=request.user, is_completed=False).first()
        return render(request, 'cart.html', {'order': order})

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

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1
    request.session['cart'] = cart
    return redirect('cart')

def cart(request):
    cart = request.session.get('cart', {})
    return render(request, 'cart.html', {'cart': cart})