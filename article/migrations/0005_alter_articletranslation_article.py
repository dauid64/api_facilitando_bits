# Generated by Django 5.1.4 on 2025-01-13 01:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_remove_article_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articletranslation',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='article.article'),
        ),
    ]
