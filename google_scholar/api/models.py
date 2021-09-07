from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from . import validators


class Organisation(models.Model):
    """
    name: str
    user: Foreign Key to User
    """
    name = models.CharField(max_length=250, help_text='Organisation Name', blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organisations')

    class Meta:
        unique_together = ['name', 'user']

    def __str__(self):
        return self.name


class Scholar(models.Model):
    """
    id: str, PRIMARY KEY (It is the only thing which needs to be inputted)
    name: str
    organisations: Many to Many Field with Organisation
    """
    id = models.CharField(max_length=20, help_text='Scholar User id', primary_key=True,
                          validators=[validators.scholar_id_validator])
    name = models.CharField(max_length=100, help_text='Scholar Name', blank=True)
    organisations = models.ManyToManyField(Organisation, blank=False, related_name='scholars')

    def __str__(self):
        return self.name


class Paper(models.Model):
    """
    id: str, PRIMARY KEY (Must be added by script)
    year: int (min -> 1000, max -> 9999)
    citation: int
    scholars: Many to Many Field with Scholar
    """
    id = models.CharField(max_length=20, primary_key=True)
    year = models.IntegerField(validators=[MinValueValidator(1000), MaxValueValidator(9999)])
    citation = models.IntegerField()
    scholars = models.ManyToManyField(Scholar, related_name='papers')

    def __str__(self):
        return self.id

