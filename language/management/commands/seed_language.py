from django.core.management.base import BaseCommand

SEED_LANGUAGES = {
    'Portuguese': 'pt',
    'English': 'en',
}

class Command(BaseCommand):
    help = 'Seed languages'

    def handle(self, *args, **options):
        from language.models import Language

        for language_name, language_code in SEED_LANGUAGES.items():
            Language.objects.get_or_create(name=language_name, code=language_code)
            self.stdout.write(self.style.SUCCESS(f'Language {language_name} created'))