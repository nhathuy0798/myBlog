from django.contrib import admin
from .models import Product, Comment_item
# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment_item
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','date']
    list_filter = ['date']
    search_fields = ['title']
    inlines = [CommentInline]
admin.site.register(Product, ProductAdmin)




