# Generated by Django 3.2.4 on 2021-07-19 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemlist',
            name='icategory',
            field=models.CharField(choices=[('Indian', 'Indian'), ('Imported', 'Imported'), ('Select item-type', 'Select item-type')], default='Select item-type', max_length=50),
        ),
    ]
