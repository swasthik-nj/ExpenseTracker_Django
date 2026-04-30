from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    # ── Authentication ──
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(
        template_name='registration/login.html',
        redirect_authenticated_user=True,
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # ── Dashboard (home page) ──
    path('', views.DashboardView.as_view(), name='dashboard'),

    # ── Transactions ──
    path('transactions/', views.TransactionListView.as_view(), name='transaction-list'),
    path('transactions/add/', views.TransactionCreateView.as_view(), name='transaction-add'),
    path('transactions/<int:pk>/edit/', views.TransactionUpdateView.as_view(), name='transaction-edit'),
    path('transactions/<int:pk>/delete/', views.TransactionDeleteView.as_view(), name='transaction-delete'),

    # ── Categories ──
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/add/', views.CategoryCreateView.as_view(), name='category-add'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),
]
