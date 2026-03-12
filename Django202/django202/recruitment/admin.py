from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Organization, JobPosting, Candidate, Resume


admin.site.register(Organization)
admin.site.register(JobPosting)
admin.site.register(Candidate)
admin.site.register(Resume)