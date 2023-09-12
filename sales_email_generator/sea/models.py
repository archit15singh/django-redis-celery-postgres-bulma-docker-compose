from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="%(app_label)s_%(class)s_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="%(app_label)s_%(class)s_updated_by")

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now().astimezone(timezone.get_current_timezone())
        self.updated_at = timezone.now().astimezone(timezone.get_current_timezone())
        super(BaseModel, self).save(*args, **kwargs)



class Prospect(BaseModel):
    name = models.CharField(max_length=255)
    website = models.URLField()
    industry = models.CharField(max_length=255)
    history = models.TextField()
    mission = models.TextField()
    core_values = models.TextField()
    solutions_offered = models.TextField()
    client_testimonials = models.TextField()
    value_proposition = models.TextField()

    def __str__(self):
        return self.name


class JobDescription(BaseModel):
    prospect = models.ForeignKey(Prospect, null=True, on_delete=models.SET_NULL)
    raw = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    job_summary = models.TextField()
    responsibilities = models.TextField()
    preferred_qualifications = models.TextField()
    company_overview = models.TextField()
    location = models.CharField(max_length=255)
    team_name = models.CharField(max_length=255)
    technology_stack = models.CharField(max_length=255)

    def __str__(self):
        return self.job_title


class Email(BaseModel):
    INTRODUCTORY = 'introductory'

    EMAIL_TYPE_CHOICES = [
        (INTRODUCTORY, 'Introductory'),
    ]

    subject = models.CharField(max_length=255)
    body = models.TextField(max_length=1000)
    type = models.CharField(max_length=20, choices=EMAIL_TYPE_CHOICES, default=INTRODUCTORY)
    job_description = models.OneToOneField(JobDescription, null=True, on_delete=models.SET_NULL)
    prospect = models.ForeignKey(Prospect, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.subject


class BackgroundJob(BaseModel):
    STATUS_CHOICES = (
        ('running', 'Running'),
        ('done', 'Done'),
        ('error', 'Error'),
    )

    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    prospect = models.ForeignKey(Prospect, null=True, on_delete=models.SET_NULL)
    email = models.OneToOneField(Email, null=True, on_delete=models.SET_NULL)
    celery_task_id = models.CharField()
