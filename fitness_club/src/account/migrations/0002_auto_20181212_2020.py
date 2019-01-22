# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_client',
            field=models.BooleanField(verbose_name='client_status', default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_employee',
            field=models.BooleanField(verbose_name='employee_status', default=False),
        ),
    ]
