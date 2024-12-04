from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=255, blank=True)
    slug = models.CharField(max_length=100, unique=True)
    cat_image = models.ImageField(upload_to = 'photos/categories',blank=True)
    
# Esto se hizo por en el Pyhton Admin salia en plural categorys por lo que se cambio a categories    
    class Meta:
        verbose_name ='category'
        verbose_name_plural ='categories'
    
    def get_url(self):
        return reverse('products_by_category', args=[self.slug])
#       ejemplo: http://localhost:8000/store/computadora    
    
    def __str__(self):
        return self.category_name
    
    
    
