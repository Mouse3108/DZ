# Generated by Django 5.1.1 on 2024-09-25 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_alter_post_category_alter_post_cover_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('approved', 'Опубликован'), ('rejected', 'Отклонен'), ('unchecked', 'На проверке')], default='unchecked', max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('published', 'Опубликовано'), ('draft', 'Черновик')], default='draft', max_length=10, verbose_name='Статус'),
        ),
    ]
