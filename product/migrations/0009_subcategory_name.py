# Generated by Django 4.2.3 on 2023-12-15 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_remove_category_product_class_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='name',
            field=models.CharField(default='', max_length=155),
            preserve_default=False,
        ),
    ]
