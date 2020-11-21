from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Student_Profile(models.Model):
    gender_choices = (  ('male','Male'),
                        ('female','Female'),
                        ('other','Other'),
                    )

    bloodGroup_choices = (  ('O+','O+'),('A+','A+'),('B+','B+'),('AB+','AB+'),
                            ('O-','O-'),('A-','A-'),('B-','B-'),('AB-','AB-'),
                    )
    semester_choices = (    ('3','3'),('4','4'),
                            ('5','5'),('6','6'),
                    )
    username = models.OneToOneField(User, on_delete = models.CASCADE)
    profilepic = models.ImageField(upload_to='profilepic/', blank=True, null=True)
    dateOfBirth = models.DateField(default = timezone.now)
    gender = models.CharField(max_length = 10, choices = gender_choices, default = 'Male')
    phoneNumber = models.CharField(max_length=10)
    course = models.CharField(max_length = 100)
    semester = models.CharField(max_length=10, choices = semester_choices, default='5')
    hobbies = models.CharField(max_length = 500)
    bloodGroup = models.CharField(max_length = 10, choices = bloodGroup_choices, default=')+')
    knownLanguages = models.CharField(max_length = 100)
    currentAddress = models.TextField()
    permanentAddress = models.TextField()
    batch = models.PositiveIntegerField()
    editStatus = models.IntegerField(default=0)


class Academic_table(models.Model):
    course_choices = (  ('SSLC','SSLC'),
                        ('PUC','PUC'),
                        ('DEGREE','DEGREE'),
                        ('MCA','MCA')
                    )
    username = models.ForeignKey(User, on_delete = models.CASCADE)
    courses = models.CharField(max_length = 50, choices = course_choices)
    college = models.CharField(max_length = 100)
    university = models.CharField(max_length = 100)
    yearOfPass = models.IntegerField()
    CGPA = models.DecimalField(max_digits=4, decimal_places=2)
    markscard = models.ImageField(upload_to = 'markscard/', blank=True, null=True)


class skills(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    languages = models.CharField(max_length=200)
    operatingSystem = models.CharField(max_length=200)
    database = models.CharField(max_length=200)
    technologies = models.CharField(max_length=200)
    applications = models.CharField(max_length=200)

class projects(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)

