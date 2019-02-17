# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_employeeprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeprofile',
            name='description',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
