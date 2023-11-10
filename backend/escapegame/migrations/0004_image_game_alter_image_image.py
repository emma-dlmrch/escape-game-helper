# Generated by Django 4.2.5 on 2023-11-10 18:42

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import escapegame.models
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('escapegame', '0003_merge_0002_image_0002_scenario_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='game',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='escapegame.game'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(base_url='/uploads', location=pathlib.PureWindowsPath('../frontend/public')), upload_to=escapegame.models.path_and_rename),
        ),
    ]
