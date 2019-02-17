# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20190130_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeprofile',
            name='description',
            field=models.TextField(max_length=500, blank=True, null=True),
        ),
    ]
