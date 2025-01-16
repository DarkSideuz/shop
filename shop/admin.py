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

# Admin class for Category model
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')  # Display category name and image in the list view
    search_fields = ('name',)

# Register models in admin
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory)
admin.site.register(Product, ProductAdmin)
