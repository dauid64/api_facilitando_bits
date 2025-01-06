from article.models import Article, Language
from rest_framework import serializers

from language.serializers import LanguageSerializer


class ArticleSerializer(serializers.ModelSerializer):
    language = LanguageSerializer()
    created_at = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S", read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'description', 'content', 'language', 'created_at', 'updated_at']

    def to_representation(self, instance):
        # Sobrescreve para converter snake_case para camelCase
        representation = super().to_representation(instance)
        camel_case_representation = {}

        for key, value in representation.items():
            camel_case_key = ''.join([key.split('_')[0]] + [word.capitalize() for word in key.split('_')[1:]])
            camel_case_representation[camel_case_key] = value

        return camel_case_representation