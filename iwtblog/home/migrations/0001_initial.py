# Generated by Django 4.1.3 on 2022-11-25 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('heading', models.CharField(max_length=600)),
                ('author', models.CharField(max_length=500)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('img', models.ImageField(upload_to='media')),
            ],
        ),
    ]
