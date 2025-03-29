from django.shortcuts import render, redirect
from .models import Product, Category
import pandas as pd

def product_list(request):
    query = request.GET.get('q')
    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    return render(request, 'product_list.html', {'products': products})


def add_product(request):
    if request.method == "POST":
        name = request.POST['name']
        category_id = request.POST['category']
        quantity = request.POST['quantity']
        
        category = Category.objects.get(id=category_id)
        Product.objects.create(name=name, category=category, quantity=quantity)
        
        update_excel()
        
        return redirect('product_list')

    categories = Category.objects.all()
    return render(request, 'add_product.html', {'categories': categories})

def update_excel():
    try:
        products = Product.objects.all().values()
        df = pd.DataFrame(products)
        excel_path = os.path.join(os.path.dirname(__file__), 'inventory.xlsx')
        df.to_excel(excel_path, index=False)
    except Exception as e:
        print(f"Error updating Excel file: {e}")


def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)
    
    if request.method == "POST":
        product.name = request.POST['name']
        product.category = Category.objects.get(id=request.POST['category'])
        product.quantity = request.POST['quantity']
        product.save()
        
        update_excel()
        
        return redirect('product_list')

    categories = Category.objects.all()
    return render(request, 'edit_product.html', {'product': product, 'categories': categories})


def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    update_excel()
    return redirect('product_list')
