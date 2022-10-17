from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=200, null=False);
    slug = models.SlugField(max_length=250, unique_for_date='published')
    url = models.ImageField(upload_to=None)