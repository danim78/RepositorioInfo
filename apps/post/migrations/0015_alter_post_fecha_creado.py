# Generated by Django 3.2.9 on 2021-12-18 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0014_alter_post_fecha_creado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='fecha_creado',
            field=models.DateField(auto_now_add=True),
        ),
    ]