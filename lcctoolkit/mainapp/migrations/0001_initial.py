# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 16:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('iso', models.CharField(max_length=2, primary_key=True, serialize=False, verbose_name='ISO')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
            ],
            options={
                'db_table': 'country',
                'ordering': ('name',),
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Legislation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('en', 'English'), ('cs', 'Czech'), ('sq-al', 'Albanian'), ('lt', 'Lithuanian'), ('hy', 'Armenian'), ('fr', 'French'), ('nl', 'Dutch'), ('ru', 'Russian'), ('tr', 'Turkish'), ('pl', 'Polish'), ('ky', 'Kyrgyz'), ('bg', 'Bulgaria'), ('de-at', 'German'), ('az-az', 'Azeri'), ('uk', 'Ukrainian'), ('tk', 'Turkmen'), ('be-by', 'Belarusian'), ('se-se', 'Sami'), ('uz', 'Uzbek'), ('sk', 'Slovak'), ('fi', 'Finnish'), ('no', 'Norwegian'), ('is', 'Icelandic'), ('de-de', 'German'), ('fr-ch', 'French'), ('de-ch', 'German'), ('it-ch', 'Italian'), ('ro', 'Romanian'), ('de-li', 'German'), ('hu', 'Hungarian'), ('bs-ba', 'Bosnian'), ('lv', 'Latvian'), ('it-it', 'Italian'), ('fr-mc', 'French'), ('sl', 'Slovenian'), ('ka', 'Georgian'), ('hr-hr', 'Croatian'), ('mk', 'Macedonian'), ('sr', 'Montenegrin'), ('ca', 'Catalan'), ('sr', 'Serbian'), ('sq', 'Albanian'), ('tg', 'Tajik'), ('kk', 'Kazakh'), ('pt-pt', 'Portuguese'), ('mt', 'Maltese'), ('et', 'Estonian'), ('fr-lu', 'French'), ('de-lu', 'German'), ('es-es', 'Spanish'), ('md', 'Moldavian'), ('da-dk', 'Danish'), ('el-gr', 'Greek')], default=('en', 'English'), max_length=64)),
                ('law_type', models.CharField(choices=[('Constitution', 'Constitution'), ('Legislation', 'Legislation'), ('Miscellaneous', 'Miscellaneous'), ('Regulation', 'Regulation'), ('Unknown', 'Unknown')], default=('Constitution', 'Constitution'), max_length=64)),
                ('full_text_file', models.CharField(max_length=32)),
                ('title', models.CharField(max_length=256)),
                ('abstract', models.CharField(max_length=1024)),
                ('year', models.IntegerField(choices=[(1945, 1945), (1946, 1946), (1947, 1947), (1948, 1948), (1949, 1949), (1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017)], default=(2017, 2017))),
            ],
        ),
        migrations.CreateModel(
            name='LegislationArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=65535)),
            ],
        ),
        migrations.CreateModel(
            name='TaxonomyClassification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(blank=True, max_length=16, unique=True)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='mainapp.TaxonomyClassification')),
            ],
            options={
                'ordering': ('code',),
                'verbose_name': 'Taxonomy Classification',
                'verbose_name_plural': 'Taxonomy Classifications',
            },
        ),
        migrations.CreateModel(
            name='TaxonomyTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TaxonomyTagGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countries', models.ManyToManyField(to='mainapp.Country')),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='current_role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_role', to='mainapp.UserRole'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='home_country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_country', to='mainapp.Country'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='roles',
            field=models.ManyToManyField(to='mainapp.UserRole'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='taxonomytag',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='mainapp.TaxonomyTagGroup'),
        ),
        migrations.AddField(
            model_name='legislationarticle',
            name='classifications',
            field=models.ManyToManyField(to='mainapp.TaxonomyClassification'),
        ),
        migrations.AddField(
            model_name='legislationarticle',
            name='legislation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Legislation'),
        ),
        migrations.AddField(
            model_name='legislationarticle',
            name='tags',
            field=models.ManyToManyField(to='mainapp.TaxonomyTag'),
        ),
        migrations.AddField(
            model_name='legislation',
            name='classifications',
            field=models.ManyToManyField(to='mainapp.TaxonomyClassification'),
        ),
        migrations.AddField(
            model_name='legislation',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Country'),
        ),
        migrations.AddField(
            model_name='legislation',
            name='tags',
            field=models.ManyToManyField(to='mainapp.TaxonomyTag'),
        ),
    ]