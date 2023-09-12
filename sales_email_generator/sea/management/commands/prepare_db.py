from sea.models import Prospect, Email, JobDescription, BackgroundJob
from sea.utils import create_fake_prospect, create_fake_job_description, create_fake_email, create_fake_backgroundjob
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = 'Populate the development database with fake data'


    def handle(self, *args, **options):
        records_size = settings.POPULATE_DEV_DB_RECORDS_SIZE

        Prospect.objects.all().delete()
        Email.objects.all().delete()
        JobDescription.objects.all().delete()
        BackgroundJob.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Data deleted successfully.'))

        for _ in range(records_size):
            prospect = create_fake_prospect()
            for __ in range(10):
                job_description = create_fake_job_description(prospect)
                email = create_fake_email(prospect, job_description)
                create_fake_backgroundjob(prospect, email)

        self.stdout.write(self.style.SUCCESS('Database populated successfully.'))
