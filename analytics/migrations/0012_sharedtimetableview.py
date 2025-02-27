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
# Generated by Django 1.9.2 on 2017-03-08 16:42


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("analytics", "0011_finalexammodalview"),
    ]

    operations = [
        migrations.CreateModel(
            name="SharedTimetableView",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("time_created", models.DateTimeField(auto_now_add=True)),
                (
                    "shared_timetable",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="analytics.SharedTimetable",
                    ),
                ),
            ],
        ),
    ]
