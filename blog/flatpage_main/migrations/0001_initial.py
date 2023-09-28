# Generated by Django 4.2.1 on 2023-09-28 20:04

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flatpages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewFlatpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name='Основной текстовый контент страницы')),
                ('text_block', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', verbose_name='Дополнительный блок текста')),
                ('flatpage', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flatpages.flatpage')),
            ],
            options={
                'verbose_name': 'Содержание страницы',
                'verbose_name_plural': 'Содержание страницы',
            },
        ),
    ]
