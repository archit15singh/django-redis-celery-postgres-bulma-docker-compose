import random

from sea.models import Prospect, Email, JobDescription, BackgroundJob

from faker import Faker

fake = Faker()

def create_fake_prospect(name=None, website=None):
    if name is None:
        name = fake.company()
    if website is None:
        website = f"https://{fake.domain_name()}{fake.uri_path()}"

    prospect = Prospect.objects.create(
        name=name,
        website=website,
        industry=fake.company_suffix(),
        history=fake.paragraph(),
        mission=fake.paragraph(),
        core_values=fake.paragraph(),
        solutions_offered=fake.paragraph(),
        client_testimonials=fake.paragraph(),
        value_proposition=fake.paragraph()
    )
    return prospect

def create_fake_job_description(prospect, raw_jd=None):
    if raw_jd is None:
        raw_jd = fake.paragraph()

    job_description = JobDescription.objects.create(
        prospect=prospect,
        raw=raw_jd,
        job_title=fake.job(),
        job_summary=fake.paragraph(),
        responsibilities=fake.paragraphs(),
        preferred_qualifications=fake.paragraph(),
        company_overview=fake.paragraph(),
        location=fake.city(),
        team_name=fake.word(),
        technology_stack=' '.join(fake.words(random.randint(3, 10)))
    )
    return job_description

def create_fake_email(prospect, job_description, type=None):
    if type is None:
        type=fake.word()

    email = Email.objects.create(
        subject=fake.sentence(),
        body=fake.paragraph(),
        type=type,
        prospect=prospect,
        job_description=job_description
    )
    return email

def create_fake_backgroundjob(prospect, email, status=None):
    if status is None:
        status = random.choice(['running', 'done', 'error'])
    
    bj_obj = BackgroundJob.objects.create(
        celery_task_id="temp",
        status=status,
        prospect=prospect,
        email=email
    )

    return bj_obj