# Generated by Django 4.2.3 on 2023-07-10 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0005_employees_images_alter_employees_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='Gender',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]