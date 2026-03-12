from django.db import migrations, models


def set_default_priority(apps, schema_editor):

    Candidate = apps.get_model("recruitment", "Candidate")

    for candidate in Candidate.objects.all():
        candidate.priority_score = 50
        candidate.save()


def reverse_priority(apps, schema_editor):

    Candidate = apps.get_model("recruitment", "Candidate")

    for candidate in Candidate.objects.all():
        candidate.priority_score = 0
        candidate.save()


class Migration(migrations.Migration):

    dependencies = [
        ("recruitment", "0001_initial"),
    ]

    operations = [

        migrations.AddField(
            model_name="candidate",
            name="priority_score",
            field=models.IntegerField(default=0),
        ),

        migrations.RunPython(
            set_default_priority,
            reverse_priority
        ),

    ]