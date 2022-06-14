# Generated by Django 3.1.1 on 2020-10-31 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0038_auto_20201030_1735'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='price',
            new_name='metacritic',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='mac_id',
        ),
        migrations.AddField(
            model_name='cart',
            name='desc',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='cart',
            name='release_date',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='cart',
            name='user_rating',
            field=models.FloatField(default=0),
        ),
    ]