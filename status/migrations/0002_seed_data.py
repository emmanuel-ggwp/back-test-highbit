# status/migrations/000X_seed_status.py
from django.db import migrations


def seed_status(apps, schema_editor):
    Status = apps.get_model("status", "Status")
    Status.objects.create(name="On progress", id=1)
    Status.objects.create(name="Done", id=2)


class Migration(migrations.Migration):

    dependencies = [
        ("status", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_status),
    ]
