# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-13 00:02
from __future__ import unicode_literals

import uuid

from django.db import migrations


def gen_uuid(apps, schema_editor):
    for model in ('account', 'leg', 'statementimport', 'statementline', 'transaction'):
        Model = apps.get_model('hordak', model)
        for row in Model.objects.all():
            row.uuid = uuid.uuid4()
            row.save()


class Migration(migrations.Migration):

    dependencies = [
        ('hordak', '0010_auto_20160912_2354'),
    ]

    operations = [
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]