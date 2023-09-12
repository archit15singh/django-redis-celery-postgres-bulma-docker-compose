from django.contrib import admin
from .models import Prospect, Email, JobDescription, BackgroundJob

class ProspectAdmin(admin.ModelAdmin):
    list_display = ('name', 'industry')
    list_filter = ('industry',)
    search_fields = ('name', 'industry')
    fields = ('name', 'industry', 'history', 'mission', 'core_values', 'solutions_offered', 'client_testimonials', 'value_proposition')

class EmailAdmin(admin.ModelAdmin):
    list_display = ('subject', 'prospect')
    list_filter = ('prospect',)
    search_fields = ('subject',)
    fields = ('subject', 'body', 'prospect', 'job_description')

class JobDescriptionAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'prospect', 'location', 'team_name', 'technology_stack')
    list_filter = ('prospect', 'location')
    search_fields = ('job_title', 'prospect__name', 'location')
    fields = ('prospect', 'job_title', 'job_summary', 'responsibilities', 'preferred_qualifications', 'company_overview', 'location', 'team_name', 'technology_stack')

class BackgroundJobAdmin(admin.ModelAdmin):
    list_display = ('status', 'prospect', 'email')
    list_filter = ('prospect',)
    fields = ('status', 'prospect', 'email')

admin.site.register(Prospect, ProspectAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(JobDescription, JobDescriptionAdmin)
admin.site.register(BackgroundJob, BackgroundJobAdmin)
