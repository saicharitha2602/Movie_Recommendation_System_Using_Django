# Generated by Django 3.2.7 on 2021-11-04 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='picture',
            field=models.ImageField(blank=True, max_length=255, upload_to='picture/'),
        ),
    ]