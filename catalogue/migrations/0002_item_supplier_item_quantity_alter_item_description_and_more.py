# Generated by Django 4.0.2 on 2022-02-09 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='SUPPLIER',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
