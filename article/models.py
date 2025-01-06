from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from language.models import Language

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = CKEditor5Field('Content', config_name='extends')
    youtube_link = models.URLField(null=True, blank=True)
    language = models.ForeignKey(Language, to_field='code', on_delete=models.PROTECT, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title