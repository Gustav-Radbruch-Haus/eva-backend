# Generated by Django 2.1.4 on 2019-07-01 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('received_on', models.DateField(auto_now_add=True)),
                ('begin', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('state', models.CharField(choices=[('PD', 'Pending'), ('AC', 'Accepted'), ('IP', 'In Progress'), ('CL', 'In Clarification'), ('FI', 'Finished'), ('XX', 'Rejected')], default='PD', max_length=2)),
                ('tenant', models.CharField(max_length=64)),
                ('appartement', models.CharField(max_length=12)),
                ('estinated_number_of_people', models.IntegerField()),
                ('phone', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('reason', models.CharField(max_length=255)),
                ('comment', models.TextField()),
            ],
        ),
    ]
