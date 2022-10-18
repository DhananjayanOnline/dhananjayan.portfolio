from email import message
from email.policy import default
from django.db import models

# Create your models here.


class MyWorks(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    client = models.CharField(max_length=100, null=True, blank=True)
    project_date = models.DateField(null=True, blank=True)
    site_url = models.CharField(max_length=100, default='#', null=True, blank=True)
    github_url = models.CharField(max_length=100, default='#', null=True, blank=True)

    class Meta:
        ordering = ['-project_date']

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Resume(models.Model):
    name = models.CharField(max_length=100, null = True, blank = True)
    file = models.FileField(null = True, blank = True)

    def __str__(self):
        return self.name
