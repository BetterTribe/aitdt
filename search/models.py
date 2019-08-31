from django.db import models

# Create your models here.


class User(models.Model):
    FEMALE = 'F'
    MALE = 'M'
    OTHERS = 'O'
    SEX_CHOICE = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHERS, 'Others'),
    ]
    age = models.PositiveSmallIntegerField(),
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICE,
        default=MALE,
    )


class Query(models.Model):
    query = models.CharField(max_length=250),
    location = models.CharField(max_length=250)
