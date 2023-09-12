import time
import random

from .models import BackgroundJob

from celery import shared_task


@shared_task
def get_llm_response(bj_obj_id):
    # simulate openAI response from API
    time.sleep(10)
    ret = random.choice(['done', 'error'])
    bj_obj = BackgroundJob.objects.get(id=bj_obj_id)
    bj_obj.status = ret
    bj_obj.save()
    return ret
