# Generated by Django 5.0.2 on 2024-03-16 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_userregistration_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
