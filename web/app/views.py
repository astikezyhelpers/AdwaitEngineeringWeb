from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# 1. View for Category List Page
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'app/category_list.html', {'categories': categories})

# 2. View for Product List Page (filtered by category)
def product_list(request, category_id):
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()  # Related name used in Product model
    return render(request, 'app/product_list.html', {'category': category, 'products': products, 'categories': categories})

# 3. View for Product Detail Page
def product_detail(request, product_id):
    categories = Category.objects.all()
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'app/product_detail.html', {'product': product, 'categories': categories})

def home_view(request):
    categories = Category.objects.all()
    return render(request, 'app/index.html', {'categories': categories})

def about_view(request):
    categories = Category.objects.all()
    return render(request, 'app/about-us.html', {'categories':categories})

def contact_view(request):
    categories = Category.objects.all()
    return render(request, 'app/contact.html', {'categories':categories})