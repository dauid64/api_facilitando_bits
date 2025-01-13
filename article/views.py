from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from article.models import ArticleTranslation, Language, Article
from rest_framework import status

from article.serializers import ArticleSerializer
from django.db.models import Prefetch

from django.shortcuts import get_object_or_404

class ArticleView(viewsets.ViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return self.queryset
    
    def get_serializer(self, object=None, many=False):
        return self.serializer_class(object, many=many)
    
    def list(self, request, *args, **kwargs):
        query_language = request.query_params.get('language', None)
        if not query_language:
            return Response({"error": "You must provide a language query parameter"}, status=status.HTTP_400_BAD_REQUEST)

        language = get_object_or_404(Language, code=query_language)
        article_translations = ArticleTranslation.objects.filter(language=language)
        
        articles = Article.objects.prefetch_related(
            Prefetch(
                'translations',
                queryset=article_translations
            )
        )

        result = []
        for article in articles:
            article_translation = article.translations.first()
            if article_translation:
                article_with_translation = {
                    'id': article.id,
                    'created_at': article.created_at,
                    'youtube_link': article.youtube_link,
                    'title': article_translation.title,
                    'description': article_translation.description,
                    'content': article_translation.content
                }
                result.append(article_with_translation)
            
        paginator = self.pagination_class()
        paginated_result = paginator.paginate_queryset(result, request)

        serializer = self.get_serializer(paginated_result, many=True)
        return paginator.get_paginated_response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        article_id = kwargs.get('pk')
        article = get_object_or_404(Article, pk=article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
