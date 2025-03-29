from django.urls import path
from .views import product_list, add_product, edit_product, delete_product
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', product_list, name="product_list"),
    path('add/', add_product, name="add_product"),
    path('edit/<int:product_id>/', edit_product, name="edit_product"),
    path('delete/<int:product_id>/', delete_product, name="delete_product"),
    path('login/', auth_views.LoginView.as_view(template_name='inventory_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]