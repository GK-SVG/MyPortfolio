# Generated by Django 3.0.6 on 2020-07-05 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200620_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='image',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
