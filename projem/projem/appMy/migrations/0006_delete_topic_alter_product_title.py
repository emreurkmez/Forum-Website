# Generated by Django 4.2.3 on 2023-08-01 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0005_topic'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Topic',
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
