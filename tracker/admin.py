from django.contrib import admin
from .models import Category, Transaction


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    list_filter = ('user',)
    search_fields = ('name',)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'category', 'amount', 'date', 'description')
    list_filter = ('type', 'category', 'date', 'user')
    search_fields = ('description',)
    date_hierarchy = 'date'
