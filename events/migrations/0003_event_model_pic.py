# Generated by Django 4.2.3 on 2023-10-18 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_event_model_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_model',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='event_photo/'),
        ),
    ]