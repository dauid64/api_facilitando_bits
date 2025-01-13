from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from language.models import Language

# Create your models here.
class Article(models.Model):
    youtube_link = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Artigo {self.id}'

class ArticleTranslation(models.Model):
    article = models.ForeignKey(Article, related_name='translations',on_delete=models.CASCADE)
    language = models.ForeignKey(Language, to_field='code', on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = CKEditor5Field('Content', config_name='extends')

    def __str__(self):
        return self.title