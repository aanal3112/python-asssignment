# Generated by Django 5.0 on 2023-12-19 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='repeatcount',
            old_name='daily_count',
            new_name='user_daily_count',
        ),
        migrations.RenameField(
            model_name='repeatcount',
            old_name='monthly_count',
            new_name='user_monthly_count',
        ),
        migrations.RenameField(
            model_name='repeatcount',
            old_name='total_count',
            new_name='user_total_count',
        ),
        migrations.RenameField(
            model_name='repeatcount',
            old_name='weekly_count',
            new_name='user_weekly_count',
        ),
        migrations.AddField(
            model_name='coupon',
            name='per_user_daily_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='coupon',
            name='per_user_total_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='coupon',
            name='per_user_weekly_count',
            field=models.IntegerField(default=0),
        ),
    ]
