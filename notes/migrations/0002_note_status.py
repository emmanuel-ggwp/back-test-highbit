# Generated by Django 5.1.5 on 2025-02-02 01:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
        ('status', '0002_seed_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='status',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='status.status'),
            preserve_default=False,
        ),
    ]
