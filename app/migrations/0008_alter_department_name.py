# Generated by Django 4.2.4 on 2023-08-28 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_department_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=255, null=True, verbose_name='名称'),
        ),
    ]
