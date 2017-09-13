# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sa_api_v2', '0003_auto_20160304_0527'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceEmail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(default=django.utils.timezone.now, db_index=True, blank=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True, db_index=True)),
                ('submission_set', models.CharField(max_length=128)),
                ('event', models.CharField(default=b'add', max_length=128, choices=[(b'add', b'On add')])),
                ('origin', models.CharField(max_length=100)),
                ('recipient_email_field', models.CharField(max_length=128)),
                ('from_email', models.EmailField(max_length=75)),
                ('bcc_email', models.EmailField(max_length=75)),
                ('subject', models.CharField(max_length=512)),
                ('body_text', models.TextField()),
                ('body_html', models.TextField()),
                ('dataset', models.ForeignKey(related_name='place_emails', to='sa_api_v2.DataSet')),
            ],
            options={
                'db_table': 'sa_api_place_email',
            },
            bases=(models.Model,),
        ),
    ]
