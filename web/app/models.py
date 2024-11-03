from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='category_images/')
    banner_image = models.ImageField(upload_to='category_banners/')

    def save(self, *args, **kwargs):
        # Open the image using Pillow
        img = Image.open(self.image)

        # Check the current resolution and resize if necessary
        if img.size != (270, 300):
            img = img.resize((270, 300), Image.LANCZOS)

            # Save the resized image back to the model
            img_io = BytesIO()
            img.save(img_io, format=img.format if img.format else 'PNG')
            self.image.save(self.image.name, ContentFile(img_io.getvalue()), save=False)

        if self.banner_image:
            banner_img = Image.open(self.banner_image)
            if banner_img.size != (1920, 968):
                banner_img = banner_img.resize((1920, 968), Image.LANCZOS)
                banner_img_io = BytesIO()
                banner_img.save(banner_img_io, format=banner_img.format if banner_img.format else 'PNG')
                self.banner_image.save(self.banner_image.name, ContentFile(banner_img_io.getvalue()), save=False)

        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/')
    description = models.TextField()

    def save(self, *args, **kwargs):
        # Open the image using Pillow
        img = Image.open(self.image)

        # Check the current resolution and resize if necessary
        if img.size != (570, 388):
            img = img.resize((570, 388), Image.LANCZOS)

            # Save the resized image back to the model
            img_io = BytesIO()
            img.save(img_io, format=img.format if img.format else 'PNG')
            self.image.save(self.image.name, ContentFile(img_io.getvalue()), save=False)

        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name