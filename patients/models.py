from django.db import models

EDUC_CHOICES = (
    ('0','None'),
    ('1','Primary level'),
    ('2','Secondary level'),
    ('3','Tertiary level'),
)

class Patient(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    height = models.DecimalField(null=True, max_digits=5, decimal_places=1)
    egplandt = models.DateField(null=True)
    egpregdt = models.DateField(null=True)
    egstage4dt = models.DateField(null=True)
    egcd4dt = models.DateField(null=True)
    egcd4v = models.PositiveIntegerField(null=True)
    edate = models.DateField()
    egweight = models.DecimalField(null=True, max_digits=5, decimal_places=1)
    enroldt = models.DateField(null=True)
    lastdt = models.DateField()
    returndt = models.DateField()
    startdt = models.DateField(null=True)
    startgprg = models.CharField(max_length=200)
    # TODO: there will be one more field coming