# Generated by Django 3.2.5 on 2021-07-30 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20210730_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilizator',
            name='cod_secret',
            field=models.CharField(default='1607f3d3-ae1a-42d9-81ed-37c26e1c08b3', max_length=100),
        ),
        migrations.AlterField(
            model_name='utilizator',
            name='parola',
            field=models.CharField(default='71c83140-9c21-43be-b858-0a0db7e01d67', max_length=100),
        ),
    ]
