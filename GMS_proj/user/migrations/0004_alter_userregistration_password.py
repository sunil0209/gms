# Generated by Django 5.0.2 on 2024-03-13 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_userregistration_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistration',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
