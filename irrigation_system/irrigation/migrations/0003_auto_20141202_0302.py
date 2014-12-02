# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('irrigation', '0002_auto_20141202_0256'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Arduino',
            new_name='Control',
        ),
        migrations.AlterField(
            model_name='soilmoisturecontrol',
            name='arduinoID',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
