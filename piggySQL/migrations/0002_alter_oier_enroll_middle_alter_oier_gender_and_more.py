# Generated by Django 4.1.5 on 2023-07-21 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piggySQL', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oier',
            name='enroll_middle',
            field=models.IntegerField(default=2023),
        ),
        migrations.AlterField(
            model_name='oier',
            name='gender',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='oier',
            name='uid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
