from django.contrib import admin
from .models import Category,Product
from atexit import register



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'price',
                    'in_stock', 'created', 'updated']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']   #how to display category in admin area
    prepopulated_fields = {'slug': ('name',)} #automatic slug is populated when name is typed





    # admin.register(Category)(admin.CategoryAdmin)
    # admin.site.register(Category)
    # admin.site.register(Product,ProductAdmin)

