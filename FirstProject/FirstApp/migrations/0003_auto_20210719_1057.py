# Generated by Django 3.2.4 on 2021-07-19 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0002_alter_itemlist_icategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userorder',
            name='desserts',
        ),
        migrations.RemoveField(
            model_name='userorder',
            name='desserts1',
        ),
        migrations.RemoveField(
            model_name='userorder',
            name='desserts_quantity',
        ),
        migrations.RemoveField(
            model_name='userorder',
            name='desserts_quantity1',
        ),
        migrations.RemoveField(
            model_name='userorder',
            name='mandi',
        ),
        migrations.RemoveField(
            model_name='userorder',
            name='mandi1',
        ),
        migrations.RemoveField(
            model_name='userorder',
            name='mandi_quantity',
        ),
        migrations.RemoveField(
            model_name='userorder',
            name='mandi_quantity1',
        ),
        migrations.RemoveField(
            model_name='userorder',
            name='starters',
        ),
        migrations.RemoveField(
            model_name='userorder',
            name='starters1',
        ),
        migrations.RemoveField(
            model_name='userorder',
            name='starters_quantity',
        ),
        migrations.RemoveField(
            model_name='userorder',
            name='starters_quantity1',
        ),
    ]
