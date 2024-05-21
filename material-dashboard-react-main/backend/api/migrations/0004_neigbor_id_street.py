# Generated by Django 5.0.3 on 2024-04-30 23:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_neigbor_id_subdivision'),
    ]

    operations = [
        migrations.AddField(
            model_name='neigbor',
            name='id_street',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.street'),
            preserve_default=False,
        ),
    ]
