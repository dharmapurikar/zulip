# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-10 05:59
from __future__ import unicode_literals

from django.db import migrations
from django.db.backends.postgresql_psycopg2.schema import DatabaseSchemaEditor
from django.db.migrations.state import StateApps

def delete_old_scheduled_jobs(apps, schema_editor):
    # type: (StateApps, DatabaseSchemaEditor) -> None
    """Delete any old scheduled jobs, to handle changes in the format of
    send_email. Ideally, we'd translate the jobs, but it's not really
    worth the development effort to save a few invitation reminders
    and day2 followup emails.
    """
    ScheduledJob = apps.get_model('zerver', 'ScheduledJob')
    ScheduledJob.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('zerver', '0086_realm_alter_default_org_type'),
    ]

    operations = [
        migrations.RunPython(delete_old_scheduled_jobs),
    ]
