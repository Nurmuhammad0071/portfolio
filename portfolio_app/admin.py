from django.contrib import admin
from portfolio_app.models import *

# Register your models here.
admin.site.register([MyInfo, Job, Site, Experience,Summary ,Skill, Portfolio, Testimonial, Contact, Link])
