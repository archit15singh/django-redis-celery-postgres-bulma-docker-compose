from .forms import EmailForm
from .models import Email, BackgroundJob
from sea.utils import create_fake_prospect, create_fake_job_description, create_fake_email, create_fake_backgroundjob
from .tasks import get_llm_response

from django.shortcuts import get_object_or_404, render, redirect



def list_email(request):
    emails = Email.objects.all()
    context = {
        'emails': emails,
    }
    return render(request, "sea/email_table.html", context)

def in_progress(request):
    background_jobs = BackgroundJob.objects.all().order_by('-created_at')[:4]
    context = {
        'background_jobs': background_jobs,
    }
    return render(request, "sea/in_progress.html", context)


def create_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            prospect = create_fake_prospect(form.cleaned_data['prospect_name'], form.cleaned_data['prospect_website'])
            job_description = create_fake_job_description(prospect, form.cleaned_data['job_description'])
            email = create_fake_email(prospect, job_description, form.cleaned_data['email_type'])
            bj_obj = create_fake_backgroundjob(prospect, email, status="running")
            
            result = get_llm_response.apply_async(args=[bj_obj.id])
            bj_obj.celery_task_id = result.id
            bj_obj.save()
            return redirect('in_progress')
    else:
        form = EmailForm()

    return render(request, 'sea/create_email.html', {'form': form})



def get_email(request, id):
    email = get_object_or_404(Email, id=id)
    context = {
        'email': email,
    }
    return render(request, "sea/email_details.html", context)

