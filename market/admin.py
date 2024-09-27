from django.contrib import admin

from .models import ProductCategory, Product, ProductGallery


# Register your models here
@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class ProductGalleryInlineAdmin(admin.TabularInline):
    model = ProductGallery
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)


    Inlines = [ProductGalleryInlineAdmin]




