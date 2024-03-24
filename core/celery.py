from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
app = Celery("core")
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Dhaka')

app.config_from_object("django.conf:settings", namespace="CELERY")

# generate daily revenue everyday.
app.conf.beat_schedule = {
	'calculate-revenue-everyday': { 
			'task': 'order.tasks.calculate_daily_revenue',
			# 'schedule': crontab(minute='*/1'),  
			'schedule': crontab(minute=0, hour=0), 
			}
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
	# print('Debugging tasks ==========> ')
	print(f'Request===> : {self.request!r}')

