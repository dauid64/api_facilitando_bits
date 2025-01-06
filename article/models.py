from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = CKEditor5Field('Content', config_name='extends')
    youtube_link = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title