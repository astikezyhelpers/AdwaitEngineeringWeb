from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from django.conf import settings

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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract form data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            
            # You can add logic to save data to the database or send an email
            # Here we are sending an email as an example
            subject = f"Contact Form Submission from {first_name} {last_name}"
            email_message = f"Name: {first_name} {last_name}\nEmail: {email}\nPhone: {phone}\nMessage:\n{message}"
            send_mail(subject, email_message, settings.DEFAULT_FROM_EMAIL, [settings.ADMIN_EMAIL])
            
            messages.success(request, "Your have contacted successfully. You will get a call soon.")
            return redirect('contact')  # Redirect back to the contact page
        else:
             messages.error(request, "There was an error with your submission. Please check the form for errors.")
    else:
        form = ContactForm()
    
    return render(request, 'app/contact.html', {'form': form, 'categories':categories})