# Generated by Django 4.1.4 on 2023-01-08 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_bought_receipt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='brand',
            field=models.CharField(blank=True, default='False', max_length=75, null=True),
        ),
    ]
