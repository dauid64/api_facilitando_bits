from django.contrib import admin

from article.models import Article, ArticleTranslation

class ArticleTranslationInline(admin.TabularInline):
    model = ArticleTranslation
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at']
    inlines = [ArticleTranslationInline]

# Register your models here.
admin.site.register(Article, ArticleAdmin)