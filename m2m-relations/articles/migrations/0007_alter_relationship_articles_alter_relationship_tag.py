# Generated by Django 4.0.4 on 2022-05-26 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_relationship_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='articles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article', verbose_name='Выбрать статью'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.tags', verbose_name='Выбрать раздел'),
        ),
    ]
