from django.db import models
from django.utils import timezone


# Create your models here.


class MyInfo(models.Model):
    image = models.FileField(upload_to='images')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateField(default=timezone.now)
    website = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    PhEmail = models.CharField(max_length=255)
    freelance = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    map = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name


class Job(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('noactive', 'NoActive')
    )
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    job = models.ForeignKey(MyInfo, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Site(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('noactive', 'NoActive')
    )
    about_title = models.CharField(max_length=255)
    happy_clients = models.CharField(max_length=255)
    projects = models.CharField(max_length=255)
    support = models.CharField(max_length=255)
    workers = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.projects


class Experience(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('noactive', 'NoActive')
    )
    summary = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.summary


class Skill(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('noactive', 'NoActive')
    )
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    knowledge = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Summary(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('noactive', 'NoActive')
    )
    summary = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    location = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.summary


class Portfolio(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('noactive', 'NoActive')
    )
    CHOICES = (
        ('filter-app', 'App'),
        ('filter-card', 'Card'),
        ('filter-web', 'Web'),
    )
    image = models.ImageField(upload_to='portfolio')
    image1 = models.ImageField(upload_to='portfolio')
    image2 = models.ImageField(upload_to='portfolio')
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=CHOICES)
    client = models.CharField(max_length=255)
    project_date = models.DateTimeField(default=timezone.now)
    project_url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('noactive', 'NoActive')
    )
    image = models.ImageField(upload_to='portfolio')
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('noactive', 'NoActive')
    )
    your_name = models.ImageField(upload_to='portfolio')
    your_email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.your_name


class Link(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('noactive', 'NoActive')
    )
    icon = models.ImageField(upload_to='portfolio')
    name = models.CharField(max_length=255)
    links = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
