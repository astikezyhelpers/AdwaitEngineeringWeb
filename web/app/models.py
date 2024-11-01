from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='category_images/')

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