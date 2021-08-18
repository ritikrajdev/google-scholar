from re import match
from requests import head
from django.core.exceptions import ValidationError


def year_validator(year: str):
    if not match('^[0-9]{4}$', year):
        raise ValidationError(f'Year {year} is not correctly defined')


def scholar_id_validator(id: str):
    url = 'https://scholar.google.com/citations?user=' + id
    status = head(url).status_code // 100
    if status != 2:
        raise ValidationError(f'No Google Scholar Exists with id {id}')
