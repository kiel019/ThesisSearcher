# Generated by Django 5.0.2 on 2024-03-17 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Thesis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('abstract', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('supervisor', models.CharField(max_length=100)),
                ('year_published', models.IntegerField()),
                ('keywords', models.ManyToManyField(related_name='theses', to='ThesisSearch.keyword')),
            ],
        ),
    ]