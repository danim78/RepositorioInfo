# Generated by Django 3.2.9 on 2021-12-21 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_rename_user_perfil_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='img_perfil',
            field=models.ImageField(default='default.jpeg', upload_to='media/user/'),
        ),
    ]