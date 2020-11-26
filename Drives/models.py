from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import auth
# Create your models here.

import datetime
def current_year():
    return datetime.date.today().year

class Company(models.Model):
    sector_choices = (('Automobile', 'Automobile'),
                    ('Banking/Financial Services/Insurance','Banking/Financial Services Insurance'),
                    ('Conglomerate', 'Conglomerate'),
                    ('Consulting','Consulting'),
                    ('Consumer Durables','Consumer Durables'),
                    ('Engineering','Engineering'),
                    ('FMCG','FMCG'),
                    ('Government/PSU', 'Government/PSU'),
                    ('Healthcare & Pharma', 'Healthcare & Pharma'),
                    ('Infrastructure', 'Infrastructure'),
                    ('IT & ITES', 'IT & ITES'),
                    ('Leasure,Travel & Tourism', 'Leasure,Travel & Tourism'),
                    ('Manufacturing', 'Manufacturing'),
                    ('Market Research', 'Market Research'),
                    ('Media & Advertising', 'Media & Advertising'),
                    ('Power/Oil/Energy', 'Power/Oil/Energy'),
                    ('R & D', 'R & D'),
                    ('Real Estate', 'Real Estate'),
                    ('Retail', 'Retail'),
                    ('Semiconductor', 'Semiconductor'),
                    ('Telecom', 'Telecom'),
                    ('Other','Other')
                    )
    jobstatus = (('Internship Only', 'Internship Only'),
                    ('Fulltime Only', 'Fulltime Only'),
                    ('Fulltime + Internship', 'Fulltime + Internship')
                    )
    status_choices = (('Open','Open'),
                     ('Close','Close')
                     )
    tier_choices = (('Tier1', 'Tier1'),
                    ('Tier2', 'Tier2'),
                    ('Tier3', 'Tier3')
                    )
    Company_Name= models.CharField(max_length=100)
    Postal_Address = models.TextField()
    About_Company = models.TextField()
    sector = models.CharField(max_length=100, choices=sector_choices, default='IT & ITES')
    Job_Description = models.TextField()
    Position = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Job_Status = models.CharField(max_length=100, choices=jobstatus, default='Fulltime Only')
    Bond_or_serviceAgreement = models.CharField(max_length=100)
    Company_website = models.CharField(max_length=100)
    Registartion_link = models.CharField(max_length=100)
    Year = models.IntegerField(default=current_year)
    Status = models.CharField(max_length=50, choices=status_choices, default='Open')
    package = models.CharField(max_length=100)
    stipend = models.CharField(max_length=100)
    tier = models.CharField(max_length=50, choices=tier_choices, default=None)

    def __str__(self):
        return self.Company_Name
    
    # def yearpublished(self):
    #     return self.Date.strftime('%Y')

class Test(models.Model):
    mode_choices = (('Online', 'ONLINE'),
                    ('Offline', 'OFFLINE')
                    )
    Company_Name = models.ForeignKey(Company, on_delete=models.CASCADE)
    TestMode = models.CharField(
        max_length=100, choices=mode_choices, default=None)
    Test_Date = models.DateField()
    Aptitude = models.BooleanField()
    Coding = models.BooleanField()
    Communication = models.BooleanField()
    GD = models.BooleanField()
    Techinacal = models.BooleanField()
    HR = models.BooleanField()


class Criteria(models.Model):
    Company_Name = models.ForeignKey(Company, on_delete=models.CASCADE)
    SSLC = models.PositiveIntegerField(default=0)
    PUC = models.PositiveIntegerField(default=0)
    UG = models.PositiveIntegerField(default=0)
    PG = models.PositiveIntegerField(default=0)


class drive(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    Company_Name = models.ForeignKey(Company, on_delete=models.CASCADE)
    Selected_status = models.BooleanField()
    Date = models.DateTimeField(auto_now=False, auto_now_add=True)
