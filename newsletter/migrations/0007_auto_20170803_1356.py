# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-03 13:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0006_categories_sort'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='newsletter.Categories'),
        ),
    ]
