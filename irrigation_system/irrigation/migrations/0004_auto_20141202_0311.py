# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('irrigation', '0003_auto_20141202_0302'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Control',
            new_name='Status',
        ),
        migrations.RemoveField(
            model_name='soilmoisturecontrol',
            name='arduinoID',
        ),
    ]
