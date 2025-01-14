from django.contrib import admin
from .models import Category, Subcategory, Product, ProductImage, ProductVideo

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductVideoInline(admin.TabularInline):
    model = ProductVideo
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ProductVideoInline]

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Product, ProductAdmin)
