from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


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
    status_choices = (('Internship Only', 'Internship Only'),
                    ('Fulltime Only', 'Fulltime Only'),
                    ('Fulltime + Internship', 'Fulltime + Internship')
                    )
    status = (('Open','Open'), ('Close','Close'))
    Company_Name= models.CharField(max_length=100)
    Postal_Address = models.TextField()
    About_Company = models.TextField()
    sector = models.CharField(max_length=100, choices=sector_choices, default='IT & ITES')
    Job_Description = models.TextField()
    Position = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Job_Status = models.CharField(max_length=100, choices=status_choices, default='Fulltime Only')
    Bond_or_serviceAgreement = models.CharField(max_length=100)
    Company_website = models.CharField(max_length=10)
    Registartion_link = models.CharField(max_length=100)
    Date = models.DateTimeField(auto_now=False, auto_now_add=True)
    Status = models.CharField(max_length=50, choices = status, default='Open')


class Test(models.Model):
    mode_choices = (('Online', 'ONLINE'),
                    ('Offline', 'OFFLINE')
                    )
    Company_Name = models.ForeignKey(Company, on_delete=models.CASCADE)
    TestMode = models.CharField(
        max_length=100, choices=mode_choices, default=None)
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
