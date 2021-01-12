# Generated by Django 3.1 on 2021-01-12 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0008_auto_20210112_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passenger',
            name='user',
        ),
        migrations.AddField(
            model_name='passenger',
            name='userId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='bookings.user_info'),
            preserve_default=False,
        ),
    ]