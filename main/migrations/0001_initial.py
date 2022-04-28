# Generated by Django 4.0.4 on 2022-04-25 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Password',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, db_index=True, max_length=200)),
                ('password', models.CharField(db_index=True, max_length=100)),
                ('user', models.IntegerField(db_index=True, max_length=100)),
            ],
        ),
    ]