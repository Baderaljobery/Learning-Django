from django.db import models

# Create your models here.
from django.db import models

APPLICATION_STATUS = [
        ("screening", "Screening"),
        ("interview", "Interview"),
        ("rejected", "Rejected"),
        ("hired", "Hired"),
    ]

class Organization(models.Model):
    name = models.CharField(max_length=255)
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class JobPosting(models.Model):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="job_postings"
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Candidate(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    priority_score = models.IntegerField(default=50)

    application_status = models.CharField(
        max_length=20,
        choices=APPLICATION_STATUS,
        default="screening"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Resume(models.Model):
    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        related_name="resumes"
    )

    file = models.FileField(upload_to="resumes/")

    ai_extracted_skills = models.JSONField(
        default=dict,
        help_text="AI extracted skills from resume"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resume of {self.candidate}"
