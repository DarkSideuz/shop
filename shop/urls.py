from django.urls import path
from .views import HomePageView, CategoryView, CheckoutView, CartView, ConfirmationView, ContactView, CategoryListView, CategoryProductsView, SingleProductView, add_to_cart, cart

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('category/', CategoryView.as_view(), name='category'),  
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('cart/', CartView.as_view(), name='cart'),
    path('confirmation/', ConfirmationView.as_view(), name='confirmation'),
    path('contact/', ContactView.as_view(), name='contact'),  
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:category_id>/', CategoryProductsView.as_view(), name='category_products'),
    path('product/<int:pk>/', SingleProductView.as_view(), name='product_detail'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'),
]

