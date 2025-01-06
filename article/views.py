from rest_framework.response import Response
from rest_framework import viewsets
from article.models import Language, Article
from rest_framework import status

from article.serializers import ArticleSerializer, LanguageSerializer

from django.shortcuts import get_object_or_404

class ArticleView(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def list(self, request, *args, **kwargs):
        query_language = request.query_params.get('language', None)
        if not query_language:
            return Response({"error": "You must provide a language query parameter"}, status=status.HTTP_400_BAD_REQUEST)

        language = get_object_or_404(Language, code=query_language)

        queryset = Article.objects.filter(language=language.code)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        article_id = kwargs.get('pk')
        article = get_object_or_404(Article, pk=article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
