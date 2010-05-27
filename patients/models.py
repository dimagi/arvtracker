from django.db import models

EDUC_CHOICES = (
    ('0','None'),
    ('1','Primary level'),
    ('2','Secondary level'),
    ('3','Tertiary level'),
)
INC_CHOICES = (
    ('1','=<100,000'),
    ('2','100,000 - 250,000'),
    ('3','250,001 - 500,000'),
    ('4','=> 500,001'),
)
PROGRAM_CHOICES = (
    ('0','self pay'),
    ('1','FTF'),
    ('2','PEPFAR'),
    ('3','MOH'),
)
TRANSI_CHOICES = (
    ('0','Initiated care at the ISS'),
    ('1','Reported transferring in'),
)
SEX_CHOICES = (
    ('0','Male'),
    ('1','Female'),
)

class Patient(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    age = models.PositiveIntegerField()
    #dob = models.DateTimeField() #i can pass a human readable name in
    #educ = models.CharField(max_length=1, choices=EDUC_CHOICES)
    #erd = models.DateTimeField()
    #hid = models.DateTimeField()
    std = models.DateField(null=True)
    #height = models.PositiveIntegerField()
    #bcd4v = models.PositiveIntegerField()
    #weight = models.PositiveIntegerField()
    #inc = models.CharField(max_length=1, choices=INC_CHOICES)
    #program = models.CharField(max_length=1, choices=PROGRAM_CHOICES)
    program = models.IntegerField()
    #transi = models.CharField(max_length=1, choices=TRANSI_CHOICES)
    #pregd = models.DateTimeField()
    date = models.DateField(null=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    enroll_d = models.DateField(null=True)
    f250v = models.PositiveIntegerField()
    f250d = models.DateField(null=True)
# go back to here: http://docs.djangoproject.com/en/dev/intro/tutorial01/ for more model stuff 

#USE THESE AFTER GETTING NEW TEST FILE:
#id = models.IntegerField() #numeric
#dob = models.DateField() #date
#enrolled = models.DateField() #date
#height = models.IntegerField() #numeric
#first_date_stage_4 = models.CharField(choices=???) #coded
#cd4d = models.DateField() #date
#cd4v = models.IntegerField() #numeric
#program = models.CharField(choices=???) #coded
#weight = models.IntegerField() #numeric
#last visit = models.DateField() #date
#status_art_last_visit = models.BooleanField() #boolean
#retd = models.DateField() #date
