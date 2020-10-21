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
    dateOfBirth = models.DateField(default = timezone.now)
    gender = models.CharField(max_length = 10, choices = gender_choices, default = 'Male')
    phoneNumber = models.CharField(max_length = 10)
    course = models.CharField(max_length = 100)
    semester = models.CharField(max_length = 10, choices = semester_choices, default='5')
    hobbies = models.CharField(max_length = 500)
    bloodGroup = models.CharField(max_length = 10, choices = bloodGroup_choices, default=')+')
    knownLanguages = models.CharField(max_length = 100)
    currentAddress = models.TextField()
    permanentAddress = models.TextField()

# STATUS_CHOICES = (
# ('draft', 'Draft'),
# ('published', 'Published'),
# )
#     title = models.CharField(max_length=250)
#     slug = models.SlugField(max_length=250,
#             unique_for_date='publish')
#     author = models.ForeignKey(User,
#             on_delete=models.CASCADE,
#             related_name='blog_posts')
#         body = models.TextField()
#         publish = models.DateTimeField(default=timezone.now)
#         created = models.DateTimeField(auto_now_add=True)
#         updated = models.DateTimeField(auto_now=True)
#         status = models.CharField(max_length=10,
#             choices=STATUS_CHOICES,
#             default='draft')