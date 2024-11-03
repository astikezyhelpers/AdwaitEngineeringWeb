from django import forms
from django.core.exceptions import ValidationError
import re

def validate_phone(value):
    # Ensure the phone number is exactly 10 digits and starts with 5, 6, 7, 8, or 9
    if not re.match(r'^[5-9]\d{9}$', value):
        raise ValidationError("Phone number must be exactly 10 digits and start with 5, 6, 7, 8, or 9.")

def validate_email(value):
    # Ensure the email has at least 3 characters before the @ symbol
    if len(value.split('@')[0]) < 3:
        raise ValidationError("Email must have at least 3 characters before the '@' symbol.")

    # Enforce strict email format or specific domains
    if not re.match(r'^[\w\.-]+@[a-zA-Z\d-]+\.[a-zA-Z]{2,}$', value):
        raise ValidationError("Enter a valid email address.")
    # Optionally restrict to certain domains
    allowed_domains = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com", "icloud.com"]
    domain = value.split('@')[-1]
    if domain not in allowed_domains:
        raise ValidationError(f"Email domain must be one of the following: {', '.join(allowed_domains)}")

class ContactForm(forms.Form):
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-input', 
            'id': 'contact-first-name',
            'placeholder': 'First Name',
            'data-constraints': '@Required'
        }),
        required=True)
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-input', 
            'id': 'contact-last-name',
            'placeholder': 'Last Name',
            'data-constraints': '@Required'
        }),
        required=True)
    email = forms.EmailField(
        validators=[validate_email],
        widget=forms.EmailInput(attrs={
            'class': 'form-input', 
            'id': 'contact-email',
            'placeholder': 'E-mail',
            'data-constraints': '@Email @Required'
        }),
        required=True)
    phone = forms.CharField(
        max_length=10,
        required=False,
        validators=[validate_phone],
        widget=forms.TextInput(attrs={
            'class': 'form-input', 
            'id': 'contact-phone',
            'placeholder': 'Phone',
            'data-constraints': '@PhoneNumber'
        })
        )
    message = forms.CharField(
        min_length=5,
        widget=forms.Textarea(attrs={
            'class': 'form-input', 
            'id': 'contact-message',
            'placeholder': 'Your Message',
            'data-constraints': '@Required'
        }), required=True)