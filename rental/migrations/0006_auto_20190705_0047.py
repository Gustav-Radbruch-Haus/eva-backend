# Generated by Django 2.2.1 on 2019-07-04 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0005_rental_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='slug',
            field=models.SlugField(),
        ),
    ]