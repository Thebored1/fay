from django.db import models
from django.utils.text import slugify

class Products(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    
    description = models.TextField(blank=True)
    image = models.ImageField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Products, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
