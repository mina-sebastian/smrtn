# Generated by Django 3.2.5 on 2021-08-01 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20210730_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executabil',
            name='program',
            field=models.FileField(upload_to='programe/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='utilizator',
            name='cod_secret',
            field=models.CharField(default='c5a479db-df35-43bf-b4f0-ca1a5754d1e4', max_length=100),
        ),
        migrations.AlterField(
            model_name='utilizator',
            name='parola',
            field=models.CharField(default='79eee80b-fe6c-47af-a94e-fa8c6f8464ff', max_length=100),
        ),
    ]
