# Generated by Django 4.2.3 on 2023-08-03 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0009_content_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('topic_count', models.PositiveIntegerField(default=0)),
                ('post_count', models.PositiveIntegerField(default=0)),
                ('response_date', models.DateTimeField(blank=True, null=True)),
                ('user_name', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
