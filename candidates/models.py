from django.db.models import Model, CharField, IntegerField, TextChoices, DateField


class Status(TextChoices):
    APPLIED = 'APPLIED', 'Applied'
    INVITED = 'INVITED', 'Invited'
    REJECTED = 'REJECTED', 'Rejected'


class Candidate(Model):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    birth_date = DateField()
    skills = CharField(max_length=1024)
    status = CharField(choices=Status.choices, default=Status.APPLIED, max_length=24)
