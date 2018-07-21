# Generated by Django 2.0.6 on 2018-07-21 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
                ('responsibility', models.CharField(blank=True, max_length=100, null=True)),
                ('current_working', models.BooleanField(default=True)),
                ('start_month', models.CharField(blank=True, max_length=20, null=True)),
                ('start_year', models.CharField(blank=True, max_length=20, null=True)),
                ('end_month', models.CharField(blank=True, max_length=20, null=True)),
                ('end_year', models.CharField(blank=True, max_length=20, null=True)),
                ('company_type', models.CharField(blank=True, max_length=100, null=True)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='career_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='career_updated_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='career_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'account_career',
            },
        ),
    ]
