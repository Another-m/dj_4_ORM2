# Generated by Django 4.0.4 on 2022-05-26 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_relationship'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relationship',
            name='articles',
        ),
        migrations.AddField(
            model_name='relationship',
            name='articles',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='choose_main', to='articles.article'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=256, verbose_name='Раздел')),
                ('articles', models.ManyToManyField(related_name='relationships', through='articles.Relationship', to='articles.article')),
            ],
        ),
        migrations.AlterField(
            model_name='relationship',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choose_main', to='articles.tags'),
        ),
    ]
