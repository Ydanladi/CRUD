from django.db import models
from django.utils.text import slugify

# Create your models here.
class customers(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    slug=models.SlugField(null=False)
    content=models.TextField()
    date_created=models.DateTimeField()


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        
        return super().save(*args, **kwargs)