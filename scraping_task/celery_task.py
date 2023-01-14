import os  
  
from celery import Celery  
from celery.schedules import crontab  
  
# Set the default Django settings module for the 'celery' program.  
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scraping_task.settings')  
  
#pass the project name in Celery(project_name)  
app = Celery('scraping_task')  
  
# Using a string here means the worker doesn't have to serialize  
# the configuration object to child processes.  
# - namespace='CELERY' means all celery-related configuration keys  
#   should have a `CELERY_` prefix.  
app.config_from_object('django.conf:settings', namespace='CELERY')  
app.autodiscover_tasks()