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
# Generated by Django 1.9.5 on 2016-08-16 02:44


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0006_student_time_created"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="social_all",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="reaction",
            name="title",
            field=models.CharField(
                choices=[
                    (b"FIRE", b"FIRE"),
                    (b"LOVE", b"LOVE"),
                    (b"CRAP", b"CRAP"),
                    (b"OKAY", b"OKAY"),
                    (b"BORING", b"BORING"),
                    (b"HARD", b"HARD"),
                    (b"EASY", b"EASY"),
                    (b"INTERESTING", b"INTERESTING"),
                ],
                max_length=50,
            ),
        ),
    ]
