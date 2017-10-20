# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 08:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lcc', '0002_auto_20171005_1247'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lcc.Country')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1024)),
                ('parent_answer', models.NullBooleanField(default=None)),
                ('order', models.IntegerField(blank=True)),
                ('gap_on', models.NullBooleanField(default=None)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('classification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lcc.TaxonomyClassification')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='lcc.Question')),
                ('tags', models.ManyToManyField(to='lcc.TaxonomyTag')),
            ],
            options={
                'verbose_name_plural': 'Questions',
                'verbose_name': 'Question',
            },
        ),
        migrations.AddField(
            model_name='answer',
            name='assessment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lcc.Assessment'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lcc.Question'),
        ),
        migrations.AlterUniqueTogether(
            name='assessment',
            unique_together=set([('user', 'country')]),
        ),
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together=set([('question', 'value')]),
        ),
    ]