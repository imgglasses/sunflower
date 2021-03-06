# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-14 02:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import parler.models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='imagenes', verbose_name='Imagen')),
                ('date', models.DateTimeField(auto_now=True)),
                ('ext_link', models.TextField(blank=True, verbose_name='Enlace')),
                ('slug', models.SlugField(blank=True)),
                ('menu', models.BooleanField(default=False, verbose_name='Menú')),
                ('main', models.BooleanField(default=False, verbose_name='Post')),
                ('navigation', models.BooleanField(default=False, verbose_name='Navegación')),
                ('footer', models.BooleanField(default=False, verbose_name='Pie de página')),
                ('footer_sec', models.BooleanField(default=False, verbose_name='Pie de página sec')),
                ('mission', models.BooleanField(default=False, verbose_name='Misión')),
                ('quote', models.BooleanField(default=False, verbose_name='Frase')),
            ],
            options={
                'verbose_name': 'Posts',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PostTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='girasol.Post')),
            ],
            options={
                'db_tablespace': '',
                'default_permissions': (),
                'managed': True,
                'db_table': 'girasol_post_translation',
                'verbose_name': 'Posts Translation',
            },
        ),
        migrations.AlterUniqueTogether(
            name='posttranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
