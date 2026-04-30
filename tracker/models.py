from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Stores expense/income categories like Food, Travel, Bills, Salary, etc.
    Each category is linked to a user so users can have custom categories.
    """
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']
        # Prevent duplicate category names per user
        unique_together = ('name', 'user')

    def __str__(self):
        return self.name


class Transaction(models.Model):
    """
    Stores individual income or expense transactions.
    Each transaction belongs to a user and a category.
    """
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='transactions')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=255, blank=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f"{self.type.title()} - ₹{self.amount} ({self.category})"
