# Generated by Django 3.1.3 on 2021-05-04 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('date', models.DateTimeField()),
                ('text', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='event_images/')),
            ],
        ),
    ]
