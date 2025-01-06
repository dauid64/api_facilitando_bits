from rest_framework import viewsets
from language.models import Language
from language.serializers import LanguageSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class LanguageView(viewsets.ReadOnlyModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

    def retrieve(self, request, *args, **kwargs):
        language_code = kwargs.get('code')

        langauge = get_object_or_404(Language, code=language_code)

        serializer = LanguageSerializer(langauge)

        return Response(serializer.data)