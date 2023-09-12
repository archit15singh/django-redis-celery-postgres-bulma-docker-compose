import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management import BaseCommand

class Command(BaseCommand):
    help = 'wait for db to be up'

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except Exception as e:
                self.stdout.write('Database unavailable, waititng 1 second...')
                self.stdout.write(str(e))
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
