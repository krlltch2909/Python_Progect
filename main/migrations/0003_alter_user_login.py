# Generated by Django 4.0.4 on 2022-04-27 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.CharField(db_index=True, max_length=100, unique=True),
        ),
    ]