# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('irrigation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arduino',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='soilmoisturecontrol',
            name='arduinoID',
            field=models.ForeignKey(to='irrigation.Arduino'),
            preserve_default=True,
        ),
    ]
