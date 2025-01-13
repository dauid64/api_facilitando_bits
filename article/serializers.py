from rest_framework import serializers
class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    youtube_link = serializers.URLField(required=False)
    created_at = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S", read_only=True)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    content = serializers.CharField()

    def to_representation(self, instance):
        # Sobrescreve para converter snake_case para camelCase
        representation = super().to_representation(instance)
        camel_case_representation = {}

        for key, value in representation.items():
            camel_case_key = ''.join([key.split('_')[0]] + [word.capitalize() for word in key.split('_')[1:]])
            camel_case_representation[camel_case_key] = value

        return camel_case_representation