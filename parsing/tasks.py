# Copyright (C) 2017 Semester.ly Technologies, LLC
#
# Semester.ly is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Semester.ly is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

from celery.decorators import periodic_task, task
from celery.task.schedules import crontab
from celery.utils.log import get_task_logger
from django.core import management
from django.conf import settings

from timetable.school_mappers import SCHOOLS_MAP
from parsing.schools.active import ACTIVE_PARSING_SCHOOLS as ACTIVE_SCHOOLS

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(hour=00, minute=00)),
    name="task_parse_current_registration_period",
    ignore_result=True,
)
def task_parse_current_registration_period(schools=None):
    """
    Parse semesters in current registration period.

    Args:
        school (str, optional): School to parse.
    """
    schools = set(schools or ACTIVE_SCHOOLS)
    for school in set(SCHOOLS_MAP) & schools:
        # Grab the most recent year.
        years = [list(SCHOOLS_MAP[school].active_semesters.items())[-1]]

        # Handle case where registration is for full academic year
        if SCHOOLS_MAP[school].full_academic_year_registration:
            if len(SCHOOLS_MAP[school].active_semesters) > 2:
                years.append(list(SCHOOLS_MAP[school].active_semesters.items())[-2])

            # Group all semesters into single parsing call for schools that
            #  cannot support parallel parsing.
            if SCHOOLS_MAP[school].single_access:
                years_and_terms = {
                    year: SCHOOLS_MAP[school].active_semesters[year][0]
                    for year in years
                }
                task_parse_school.delay(school, years_and_terms)
                continue

        # Create individual parsing tasks.
        for year, terms in years:
            task_parse_school.delay(school, {year: [terms[0]]})


@task()
def task_parse_active(schools=None):
    """
    Parse all semesters displayed to users (i.e. active semesters).

    Args:
        school (str, optional): School to parse.
    """
    schools = set(schools or ACTIVE_SCHOOLS)
    for school in set(SCHOOLS_MAP) & schools:
        if SCHOOLS_MAP[school].singe_access:
            task_parse_school.delay(school, SCHOOLS_MAP[school].active_semesters)
            continue

        for year, terms in list(SCHOOLS_MAP[school].active_semesters.items()):
            for term in terms:
                task_parse_school.delay(school, {year: [term]})


@task()
def task_parse_school(school, years_and_terms):
    """
    Call the django management commands to start parse.

    Args:
        school (str): School to parse.
        years_and_terms (dict): Years and terms dictionary.
    """
    logger.info("Starting parse for " + school + " " + str(years_and_terms))
    filename = "{}/schools/{}/data/courses_{}.json".format(
        settings.PARSING_MODULE,
        school,
        "-".join(
            "{}{}".format(year, "".join(terms))
            for year, terms in list(years_and_terms.items())
        ),
    )

    management.call_command(
        "ingest",
        school,
        years_and_terms=years_and_terms,
        display_progress_bar=False,
        verbosity=0,
        output=filename,
    )
    management.call_command(
        "digest",
        school,
        display_progress_bar=False,
        verbosity=0,
        data=filename,
    )
    logger.info("Finished parse for " + school + " " + str(years_and_terms))
