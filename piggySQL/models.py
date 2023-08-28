from django.db import models

# Create your models here.


class Record(models.Model):
    contest = models.CharField(max_length=10)
    uid = models.IntegerField("OIer", default=0)
    school = models.IntegerField()
    score = models.CharField(max_length=10)
    rank = models.IntegerField()
    Province = models.IntegerField()
    level = models.IntegerField()


class Oier(models.Model):
    name = models.CharField(max_length=10, default="")
    gender = models.IntegerField(default=0)
    records = models.ManyToManyField(to="Record")
    enroll_middle = models.IntegerField(default=2023)
    CCF_Score = models.DecimalField(
        max_length=10, max_digits=10, decimal_places=3)
    CCF_level = models.IntegerField()
    OIerDB_score = models.DecimalField(
        max_length=10, max_digits=10, decimal_places=3)
    uid = models.IntegerField(primary_key=True)
    initial = models.CharField(max_length=10)


class School(models.Model):
    name = models.CharField(max_length=10)
    ProvinceName = models.CharField(max_length=10)
    CityName = models.CharField(max_length=10)
    Score = models.DecimalField(max_length=10, max_digits=10, decimal_places=3)
    id = models.IntegerField(primary_key=True)
