from django.contrib import admin
from .models import Candidate, Resume, Organization, JobPosting


class ResumeInline(admin.TabularInline):
    model = Resume
    extra = 1


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):

    list_display = (
        "first_name",
        "last_name",
        "email",
        "priority_score",
        "application_status"
    )

    search_fields = (
        "first_name",
        "last_name",
        "email"
    )

    list_filter = (
        "application_status",
        "created_at"
    )

    inlines = [ResumeInline]


admin.site.register(Organization)
admin.site.register(JobPosting)
admin.site.register(Resume)
