# Generated by Django 3.0.2 on 2020-01-07 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('std', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('frmale', 'Female')], default='male', max_length=100)),
                ('stdid', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
