from django.contrib.auth.models import User
from django.db import models

from . import validators


class Organisation(models.Model):
    """
    Model of organisation/team to be Added
    name: str
    user: Foreign Key to User
    """
    name = models.CharField(max_length=250, help_text='Organisation Name', blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Scholar(models.Model):
    """
    Model of Scholar
    id: str, PRIMARY KEY (It is the only thing which needs to be inputted)
    name: str
    organisations: Many to Many Field with Organisation
    """
    id = models.CharField(max_length=20, help_text='Scholar User id', primary_key=True,
                          validators=[validators.scholar_id_validator])
    name = models.CharField(max_length=100, help_text='Scholar Name', blank=True)
    organisations = models.ManyToManyField(Organisation, blank=True)

    def __str__(self):
        return self.name


class Paper(models.Model):
    """
    Model of Research Paper Published
    title: str
    url: url
    year: str (format 'yyyy')
    author: str
    citation: int
    """
    title = models.CharField(max_length=200)
    url = models.URLField()
    author = models.OneToOneField(Scholar, on_delete=models.CASCADE)
    year = models.CharField(max_length=4, validators=[validators.year_validator])
    citation = models.IntegerField()

    def __str__(self):
        return self.title
