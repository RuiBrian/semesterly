"""
Copyright (C) 2017 Semester.ly Technologies, LLC

Semester.ly is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Semester.ly is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-28 18:24


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0008_auto_20160815_2150"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="emails_enabled",
            field=models.NullBooleanField(default=True),
        ),
    ]
