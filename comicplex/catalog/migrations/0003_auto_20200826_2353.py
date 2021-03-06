# Generated by Django 3.0.7 on 2020-08-26 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20200826_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comic',
            name='artists',
            field=models.ManyToManyField(help_text='Enter name of artists', related_name='artist_comics', to='catalog.Person'),
        ),
        migrations.AlterField(
            model_name='comic',
            name='colors',
            field=models.ManyToManyField(help_text='Enter name of writers', related_name='colors_comics', to='catalog.Person'),
        ),
        migrations.AlterField(
            model_name='comic',
            name='covers',
            field=models.ManyToManyField(help_text='Enter name of writers', related_name='covers_comics', to='catalog.Person'),
        ),
        migrations.AlterField(
            model_name='comic',
            name='inks',
            field=models.ManyToManyField(help_text='Enter name of writers', related_name='inks_comics', to='catalog.Person'),
        ),
        migrations.AlterField(
            model_name='comic',
            name='letters',
            field=models.ManyToManyField(help_text='Enter name of writers', related_name='letters_comics', to='catalog.Person'),
        ),
        migrations.AlterField(
            model_name='comic',
            name='writers',
            field=models.ManyToManyField(help_text='Enter name of writers', related_name='writer_comics', to='catalog.Person'),
        ),
    ]
