# Generated by Django 4.2 on 2023-04-16 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_categoriaproductos_nombrecate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoriaproductos',
            name='nombrecate',
            field=models.CharField(max_length=30, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='idProducto',
            field=models.CharField(max_length=5, primary_key=True, serialize=False),
        ),
    ]
