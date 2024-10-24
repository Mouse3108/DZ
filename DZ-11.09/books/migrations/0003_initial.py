# Generated by Django 4.1 on 2024-09-11 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0002_delete_books'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('publish_year', models.IntegerField()),
                ('is_bestseller', models.BooleanField(default=False)),
            ],
        ),
    ]
