from django.urls import path
from .views import HomePageView, CategoryView, SingleProductView, CheckoutView, CartView, ConfirmationView, ContactView, CategoryListView
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('category/', CategoryView.as_view(), name='category'),
    path('product/<int:pk>/', SingleProductView.as_view(), name='single_product'),  # <int:pk> - mahsulot ID
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('cart/', CartView.as_view(), name='cart'),
    path('confirmation/', ConfirmationView.as_view(), name='confirmation'),
    path('contact/', ContactView.as_view(), name='contact'),  # Contact URL yo'li
    path('categories/', CategoryListView.as_view(), name='category_list'),
]

