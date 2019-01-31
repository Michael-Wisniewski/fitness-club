# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import slider_backend.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SliderPicture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('image', models.ImageField(upload_to=slider_backend.models.slider_directory_path)),
                ('order', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), slider_backend.models.validate_nonzero])),
            ],
        ),
    ]
