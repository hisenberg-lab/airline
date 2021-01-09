# Generated by Django 3.1 on 2021-01-08 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0006_auto_20210108_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='trip_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bookings.flight_trip'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='seat',
            unique_together={('id', 'trip_id')},
        ),
    ]