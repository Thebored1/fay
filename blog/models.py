from django.db import models
from django.utils.text import slugify

class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    content = models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
