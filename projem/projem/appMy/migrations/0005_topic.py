# Generated by Django 4.2.3 on 2023-08-01 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0004_category_product_delete_konu_post_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('sub_forum', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
    ]
