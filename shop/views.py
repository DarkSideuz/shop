# shop/views.py
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class CategoryView(TemplateView):
    template_name = 'category.html'  # Sizning category.html faylingiz bo'lishi kerak

class SingleProductView(TemplateView):
    template_name = 'single_product.html'  # Sizning single_product.html faylingiz bo'lishi kerak

class CheckoutView(TemplateView):
    template_name = 'checkout.html'  # Sizning checkout.html faylingiz bo'lishi kerak

class CartView(TemplateView):
    template_name = 'cart.html'  # Sizning cart.html faylingiz bo'lishi kerak

class ConfirmationView(TemplateView):
    template_name = 'confirmation.html'  # Sizning confirmation.html faylingiz bo'lishi kerak

class SingleProductView(TemplateView):
    template_name = 'single-product.html'

class ContactView(TemplateView):
    template_name = 'contact.html'  # Sizning contact.html faylingiz bo'lishi kerak