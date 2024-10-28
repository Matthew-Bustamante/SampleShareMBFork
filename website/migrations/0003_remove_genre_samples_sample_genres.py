# Generated by Django 5.1.1 on 2024-10-28 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_genre_genrename_alter_genre_samples'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='samples',
        ),
        migrations.AddField(
            model_name='sample',
            name='genres',
            field=models.ManyToManyField(blank=True, related_name='samples', to='website.genre'),
        ),
    ]
