from django.db import models 
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Page(models.Model):  
    title = models.CharField(max_length=200) 
    slug = models.SlugField(max_length=255,  null= True, unique=True)
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(blank=True)
    content = RichTextField() 

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('page', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)
