# Generated by Django 4.1.4 on 2022-12-19 14:33

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_rename_clubid_user_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]