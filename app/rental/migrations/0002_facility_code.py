# Generated by Django 2.2.1 on 2019-07-07 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='facility',
            name='code',
            field=models.CharField(default='TR', max_length=4),
            preserve_default=False,
        ),
    ]