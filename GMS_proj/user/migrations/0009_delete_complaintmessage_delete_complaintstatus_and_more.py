# Generated by Django 5.0.2 on 2024-03-21 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_delete_adminregistration'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ComplaintMessage',
        ),
        migrations.DeleteModel(
            name='ComplaintStatus',
        ),
        migrations.DeleteModel(
            name='CreateComplaint',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Designation',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='ProfileType',
        ),
        migrations.DeleteModel(
            name='UserRegistration',
        ),
    ]
